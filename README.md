# FastAPI App with Agents

這是一個使用 FastAPI 建立的 Web 應用程式，整合了 Hugging Face 的工具與 SmolAgents，以實現各種查詢與 API 功能。

## 功能說明rftedr

1. **整合 Hugging Face 平台**  
   登錄 Hugging Face Token 並使用其模型功能進行自然語言處理。

2. **使用 SmolAgents**  
   - **CodeAgent**: 用於處理查詢的核心代理。
   - **DuckDuckGoSearchTool**: 支援網頁搜尋的工具。
   - **HfApiModel**: Hugging Face API 模型，用於回應查詢。

3. **API 路由**  
   - `/query`: 提供一個簡單的查詢功能，回傳問題與答案。
   - `/`: 根路徑，顯示歡迎訊息。
   - `/api/測試`: 根據輸入名稱返回對應的回應資訊。

## 程式結構

- **Hugging Face 登錄**
  登錄使用者 Token 以存取 Hugging Face 的功能。

- **工具與模型的初始化**
  定義與初始化代理工具以處理查詢需求。

- **FastAPI 路由**
  透過多個 API 路由處理查詢並回應對應的資料。

## 使用方式

1. **環境準備**
   確保已安裝所需的 Python 套件：
   ```bash
   pip install fastapi uvicorn huggingface_hub smolagents
