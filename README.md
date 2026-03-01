# notebook

一个纯前端、完全离线的本地记账本。

当前版本只保留单文件应用 [`记账本.html`](./记账本.html)。双击即可打开，数据保存在浏览器本地 `localStorage` 中，不依赖后端服务。

## 功能

- 新增收入/支出记录
- 币种选择，默认 `RMB`
- 按币种分别汇总收入、支出、结余
- 删除记录
- 导出备份 `JSON`
- 导入备份 `JSON`
- 清空全部记录

## 使用方式

直接双击打开：

- `记账本.html`

或在浏览器中手动打开该文件。

## 数据说明

- 数据存储在浏览器本地 `localStorage`
- 不会写入服务器
- 不同浏览器之间不会自动同步
- 清除浏览器站点数据后，本地记录可能被清空

## 测试

运行回归测试：

```bash
python3 -m unittest discover -s tests -v
```

或直接双击：

- `回归测试.command`

当前测试主要覆盖：

- 离线单文件界面结构
- 币种选项与默认值
- 本地存储逻辑
- 导入、导出、清空等关键入口

详细规则见：

- [`测试验收标准.md`](./测试验收标准.md)

## Git 工作流

当前稳定分支：

- `master`

当前版本已先发布到 `master`。后续新需求按以下流程开发：

1. 从 `master` 拉新分支
2. 在功能分支开发
3. 本地跑测试
4. 测试通过后合并回 `master`

示例：

```bash
git checkout master
git pull origin master
git checkout -b feature/your-feature

# 开发完成后
python3 -m unittest discover -s tests -v
git add .
git commit -m "实现：你的功能"
git push -u origin feature/your-feature

# 确认通过后合并
git checkout master
git pull origin master
git merge feature/your-feature
git push origin master
```

## 仓库命名建议

- 仓库名建议使用全小写
- 多单词时建议使用连字符 `-`

当前仓库名 `notebook` 符合常见约定。
