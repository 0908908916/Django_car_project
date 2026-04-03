作品介紹 — Django 汽車車輛管理系統

📌 作品名稱
Django 汽車車輛管理後台系統
🛠️ 使用技術

後端框架：Python Django 4.2
資料庫：SQLite（開發）/ 可擴充至 PostgreSQL
前端：HTML5、Bootstrap 5、Django Template
其他：Pillow（圖片處理）、Django Admin


📋 作品說明
本專案為一套完整的汽車車輛管理後台系統，涵蓋前台展示與後台管理功能，模擬真實汽車業者的內部管理需求。
從資料庫設計、後端邏輯、表單驗證到前端介面，皆獨立完成，並實作使用者認證、資料篩選與表單送出等完整功能流程。

✅ 功能特色

車款列表與詳細頁：卡片式排版展示所有車款，點擊可查看完整規格與說明
搜尋與篩選功能：支援關鍵字搜尋、燃料類型、價格區間等多條件篩選
會員系統：包含註冊、登入、登出功能，整合 Django 內建認證機制
詢價 / 預約表單：訪客可針對特定車款送出詢價申請，資料即時寫入資料庫
後台管理介面：透過 Django Admin 管理品牌、車款上下架、詢價單狀態追蹤


📁 專案架構
car_project/
├── car_project/         # 主設定（settings、urls）
└── cars/                # 核心 App
    ├── models.py        # 資料模型（Brand、Car、Inquiry）
    ├── views.py         # 邏輯處理
    ├── urls.py          # 路由設定
    ├── forms.py         # 表單驗證
    ├── admin.py         # 後台管理設定
    └── templates/       # HTML 模板

💡 開發過程與學習心得
本專案從零開始建置，完整走過以下開發流程：

規劃資料庫結構（品牌、車款、詢價三張資料表）
設計 Django Model 並透過 Migration 建立資料庫
撰寫 View 處理各頁面邏輯與表單資料
設定 URL 路由對應各功能頁面
使用 Django Template 搭配 Bootstrap 5 完成前端介面
整合 Django 內建 Auth 完成會員登入系統
設定 Django Admin 建立後台管理功能
除錯與調整（含虛擬環境設定、模組找不到等實務問題排除）

透過此專案，實際理解了 Django 的 MTV 架構（Model、Template、View）、ORM 查詢、表單驗證流程，以及 Django Admin 的客製化設定，具備獨立開發中小型 Web 應用的能力。

🔗 專案資訊

開發時間：2026 年
開發人員：個人獨立開發
開發環境：Windows、Python 3.10、Django 4.2

建立後台管理員帳號
python manage.py createsuperuser

建立資料庫
python manage.py makemigrations
python manage.py migrate

開啟專案
python manage.py runserver
