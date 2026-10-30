# JoyHome UK — 網站改版概念設計

[joyhomeuk.com](https://joyhomeuk.com/) 的改版提案。純靜態網站（HTML / CSS / JS），不需要建置步驟，任何靜態主機都能直接部署。

> **概念設計展示**：由 [UX CIRCLES](https://ux-circles.com/web) 設計，並非 JoyHome UK 官方網站。
> 每頁頂端有「Concept」標示列，所有頁面設為 `noindex`，`robots.txt` 禁止搜尋引擎收錄。
> 如果正式採用：刪掉 `_build/build.py` 裡的 `.concept-bar` 及 `noindex`，重新生成，並把 `robots.txt` 改回 `Allow: /`。

## 頁面

| 檔案 | 內容 |
|---|---|
| `index.html` | 首頁：四個不同之處、服務、三步流程、收費摘要、六種英國房屋、FAQ、認證及合作伙伴 |
| `services.html` | 服務及收費（諮詢、租樓、買樓、代睇樓、外加代辦） |
| `buy.html` | 英國買樓：熱門地區、二手 / 一手流程、印花稅、Milton Keynes、FAQ |
| `rent.html` | 英國租屋：流程、Reference check 文件、FAQ |
| `management.html` | 物業管理（JHPM） |
| `renovation.html` | 英國裝修（JoyHome Builder） |
| `contact.html` | 聯絡：查詢表會把資料整理成 WhatsApp 或電郵訊息，不需要伺服器 |

## 修改方式

所有頁面由 `_build/build.py` 生成（共用頁首、頁尾、聯絡資料）。改內容後執行：

```bash
python3 _build/build.py
python3 -m http.server 5173   # 預覽 http://localhost:5173
```

電話、WhatsApp、電郵、PRS 編號都在 `build.py` 頂部。改了 CSS / JS 記得把 `CSS_V` / `JS_V` +1。

## 設計

- 顏色沿用原站品牌：海軍藍 `#1F4670`（原 `#234E79` 稍加深）+ 金啡 `#BDAF8E`
- 字體：Noto Serif TC（標題）+ Noto Sans TC（內文）
- 圖片全部來自原站，轉為 WebP

## 上線前待確認

- [ ] **電話號碼**：原站顯示 +44 7511 817812，但頁尾連結是 +44 7528 961365。本站統一用前者，請確認
- [ ] **印花稅表**已更新為 2025 年 4 月起稅率（原站是 2022 年舊稅率，並把非居民附加稅寫成 5%，實際為 2%），請以 GOV.UK 再核實
- [ ] **租屋**：原站「預繳 6–12 個月租金」的說法已移除，英格蘭 2026 年起實施 Renters' Rights Act，請按最新法例補充
- [ ] Milton Keynes 樓盤價錢是 2022 年資料，已標示為「過往樓盤，只作參考」
- [ ] 首頁「睇樓分析」卡片是示例內容，已標示「示例」
- [ ] 其他城市（London、Birmingham 等）的獨立頁面未重做，目前連到聯絡頁
- [ ] 辦公時間「星期六、日休息」是推斷，請確認
