# Mini Kimi CLI (Refactored)

这是一个从 Kimi CLI 核心架构拆解出来的最小化实现 demo。代码已重构为模块化结构。

## 目录结构

请参考 `docs/结构说明.md`。

## 运行前准备

1.  安装依赖：
    ```bash
    pip install openai duckduckgo-search
    ```

2.  设置 API Key（使用 Moonshot AI 的 Key）：
    - Windows (PowerShell): `$env:MOONSHOT_API_KEY="your_key"`
    - Linux/Mac: `export MOONSHOT_API_KEY="your_key"`

## 运行

在项目根目录下运行（需要设置 PYTHONPATH 以便找到模块）：

**Windows (PowerShell):**
```powershell
$env:PYTHONPATH="mini_kimi/src"
python mini_kimi/src/mini_kimi/ui/shell/main.py
```

**Linux/Mac:**
```bash
PYTHONPATH=mini_kimi/src python mini_kimi/src/mini_kimi/ui/shell/main.py
```

## 功能

支持以下工具：
- **Bash**: 执行 Shell 命令。
- **WriteFile**: 写文件。
- **SearchWeb**: 联网搜索 (DuckDuckGo)。
- **FetchURL**: 读取网页内容。
