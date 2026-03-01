from __future__ import annotations

import unittest
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[1]
OFFLINE_HTML = PROJECT_DIR / "记账本.html"


class OfflineHtmlRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.html = OFFLINE_HTML.read_text(encoding="utf-8")

    def test_offline_html_contains_core_ui(self) -> None:
        self.assertIn("<title>离线记账本</title>", self.html)
        self.assertIn('id="entryForm"', self.html)
        self.assertIn('id="entryTableBody"', self.html)
        self.assertIn('id="summaryGrid"', self.html)
        self.assertIn("导出备份", self.html)
        self.assertIn("导入备份", self.html)
        self.assertIn("清空全部", self.html)

    def test_offline_html_contains_currency_selector_with_rmb_default(self) -> None:
        self.assertIn('id="currency"', self.html)
        self.assertIn('<option value="RMB" selected>RMB</option>', self.html)
        self.assertIn('<option value="USD">USD</option>', self.html)
        self.assertIn('<option value="EUR">EUR</option>', self.html)
        self.assertIn("var CURRENCIES = ['RMB', 'USD', 'EUR', 'HKD', 'JPY'];", self.html)
        self.assertIn("currency.value = 'RMB';", self.html)

    def test_offline_html_uses_local_storage_and_normalizes_entries(self) -> None:
        self.assertIn("offline-ledger-entries-v1", self.html)
        self.assertIn("localStorage.getItem(STORAGE_KEY)", self.html)
        self.assertIn("localStorage.setItem(STORAGE_KEY, JSON.stringify(entries))", self.html)
        self.assertIn("function normalizeEntry(entry, index)", self.html)
        self.assertIn("currency: normalizedCurrency", self.html)
        self.assertIn("totalsByCurrency.RMB", self.html)

    def test_offline_html_keeps_backup_import_export_flow(self) -> None:
        self.assertIn("function exportEntries()", self.html)
        self.assertIn("function importEntries(file)", self.html)
        self.assertIn("reader.readAsText(file, 'utf-8');", self.html)
        self.assertIn("window.confirm('确认清空全部账目吗？此操作不能撤销。')", self.html)
        self.assertIn("render();", self.html)


if __name__ == "__main__":
    unittest.main(verbosity=2)
