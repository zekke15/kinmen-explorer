# 金門探索指南 | Kinmen Explorer

以景點、飲食、文化與旅遊靈感為主題的金門介紹網站。這是一份以 **AGENTS.md 為核心**的可持續擴充網站專案。

## 網站功能

- **首頁**：金門主題插畫、分類入口、精選景點。
- **景點探索**：依主題篩選與即時關鍵字搜尋。
- **景點詳細介紹**：一個 `detail.html?id=...` 模板對應所有景點，不需要逐頁複製 HTML。
- **在地美食**：四種在地飲食介紹。
- **歷史文化**：戰地、閩南建築、民俗與自然。
- **旅遊提案**：彈性示範行程與資訊確認提醒。

## 如何開啟

最簡單：下載／解壓縮後，直接雙擊 `index.html` 即可在瀏覽器預覽。所有頁面都使用相對路徑。

也可用 VS Code Live Server，或在專案資料夾執行：

```bash
python -m http.server 8000
```

然後瀏覽 `http://localhost:8000`。

## GitHub Pages 部署

1. 在 GitHub 建立公開 repository，例如 `kinmen-explorer`。
2. 將本專案 **所有檔案**上傳到 repository 根目錄（請勿只上傳 ZIP）。
3. GitHub Repository → **Settings → Pages**。
4. **Build and deployment** 選 `Deploy from a branch`。
5. Branch 選 `main`，資料夾選 `/(root)`，按 **Save**。
6. Pages 部署完成後，網址通常為：`https://你的帳號.github.io/kinmen-explorer/`。

> 若 repository 名稱不同，網址中的路徑也應跟著更改；必須在 Pages 顯示部署成功後才可視為已公開。

## 專案結構

```text
index.html
attractions.html
detail.html
food.html
culture.html
guide.html
content/places.js
assets/style.css
assets/app.js
assets/hero.svg
AGENTS.md
README.md
```

## AGENTS.md 如何幫助 AI 持續開發？

規則明確指定：技術限制、檔案分工、命名慣例、景點資料欄位、分類清單、設計系統、資料來源及測試流程。未來如果要加「建功嶼」，AI 只需要查核資料、在 `content/places.js` 加一筆記錄，景點列表就會自動生成卡片，詳細頁也會直接使用相同模板。若要新增新的主題頁，則依照現有 HTML 框架、新增導航並更新 README，不必重新思考網站規則。

## 如何測試

- `index.html` 可開啟且主要導覽正確。
- `attractions.html` 的「戰地記憶」分類只顯示對應景點。
- 搜尋「金城」會顯示金城鎮的景點。
- 點擊「莒光樓」進入 `detail.html?id=juguang-tower` 並可返回。
- 測試手機窄螢幕的版面與操作。

## 參考資料與圖片聲明

主要參考：[金門觀光旅遊網](https://kinmen.travel/zh-tw)、[官方必遊景點](https://kinmen.travel/zh-tw/travel/top-ten)、[官方旅遊懶人包](https://kinmen.travel/zh-tw/discover/travel-guide)。介紹文字由本站整理改寫，非官方公告；參觀資訊以官方最新公告為準。首頁 `assets/hero.svg` 是為本站製作的原創向量插畫；景點卡片為 emoji 示意圖，不代表真實照片。

## 課程繳交資料（自行補齊）

- 學校：國立金門大學
- 系級：資工（請補年級）
- 學號：**請填入**
- 姓名：**請填入**
- Repository：**請填入實際 GitHub 連結**
- 網站：**請填入實際 Pages 網址**


## 互動功能（v2）

- 景點即時搜尋、主題分類、鄉鎮篩選、排序與清除條件
- 隨機探索一個符合目前條件的景點
- 愛心收藏，可只顯示已收藏的景點
- 加入／移除我的行程、使用 ↑ ↓ 更換順序、複製成純文字、清空行程
- 收藏與行程存於瀏覽器 `localStorage`，不需要會員或後端；不同裝置不會同步

### 部署
將**此資料夾內的所有檔案**直接放在 GitHub Repository 根目錄（不要多包一層），設定 Settings → Pages → Deploy from branch → main → /(root)。

### 測試步驟
1. 開啟 `attractions.html`，搜尋「莒光樓」，測試鄉鎮與分類篩選。
2. 收藏一個景點，勾選「只看我的收藏」。
3. 加入兩個景點到行程，前往 `guide.html` 測試順序調整與複製。
4. 重新整理網頁，確認收藏與行程保留。
5. 用手機版檢查排版，並確認返回與詳細頁正常。
