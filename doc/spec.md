# lang-ast-analyze 语法树结构说明

## 语法树结构

- `sentence`: 输入的句子
- `root`: 根节点
  - `verb`: 动词（谓语）
  - `subject`: 主语
  - `object`: 宾语

## 示例

```json
{
  "sentence": "The cat chased the mouse.",
  "root": {
    "verb": "chased",
    "subject": "cat",
    "object": "mouse"
  }
}
