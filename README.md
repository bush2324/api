# 🌟 FastAPI App with Agents

這是一個使用 **FastAPI** 建立的 Web 應用程式，整合了 **Hugging Face** 的工具與 **SmolAgents**，以實現各種查詢與 API 功能。

---

## 🚀 功能說明

1. **整合 Hugging Face 平台**\
   登錄 Hugging Face Token 並使用其模型功能進行自然語言處理。

2. **使用 SmolAgents**

   - **CodeAgent**: 用於處理查詢的核心代理。
   - **DuckDuckGoSearchTool**: 支援網頁搜尋的工具。
   - **HfApiModel**: Hugging Face API 模型，用於回應查詢。

3. **API 路由**

   - `/query`: 提供一個簡單的查詢功能，回傳問題與答案。
   - `/`: 根路徑，顯示歡迎訊息。
   - `/api/測試`: 根據輸入名稱返回對應的回應資訊。

---

## 🛠️ 程式結構

- **Hugging Face 登錄**\
  登錄使用者 Token 以存取 Hugging Face 的功能。

- **工具與模型的初始化**\
  定義與初始化代理工具以處理查詢需求。

- **FastAPI 路由**\
  透過多個 API 路由處理查詢並回應對應的資料。

---

## 📘 使用方式

### 1️⃣ 環境準備

確保已安裝所需的 Python 套件：

```bash
pip install fastapi uvicorn huggingface_hub smolagents
```

### 2️⃣ 啟動服務器

使用以下指令啟動 FastAPI 伺服器：

啟動服務器（默認端口）

```bash
uvicorn main:app --reload
```

指定端口號

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 3️⃣ 測試 API

使用 curl 測試 API 路徑：

```bash
curl -X GET "http://localhost:1234/query?question=你的問題"
curl -X GET "http://localhost:1234/api/測試?name=葉家豪"
```

### 4️⃣ 生成 `requirements.txt`

指導用戶如何保存依賴文件：

```bash
pip freeze > requirements.txt
```

### 5️⃣ 虛擬環境建置（選擇性）

如果需要分離開發環境，可以創建虛擬環境：

```bash
# 創建虛擬環境
python -m venv venv
source venv/bin/activate  # Windows 使用 venv\Scripts\activate

# 安裝依賴
pip install -r requirements.txt
```

---

## 🔗 測試用網址

- **Swagger Docs**: [http://127.0.0.1:1234/docs](http://127.0.0.1:1234/docs)
- **ReDoc**: [http://127.0.0.1:1234/redoc](http://127.0.0.1:1234/redoc)

---

## ⚠️ 注意事項

- **Hugging Face Token**\
  請替換程式碼中的 `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` 為你的專屬 Token。

- **API 回應範例**

  - `葉家豪`: 回傳 `超雄聖體`
  - `溫維智`: 回傳 `旗津第一長髮男`
  - 其他名稱: 回傳 `未知的人物`

- **除錯模式**\
  使用 `reload=True` 可在開發時即時更新程式碼變更。

---

## 🌈 未來優化

- 移除重複定義的路由以提升程式碼可維護性。
- 增加更多查詢功能或動態代理模型的選擇。
- 增加錯誤處理與日誌記錄功能以改善使用者體驗。

---

🎉 **感謝使用 FastAPI App with Agents！**

