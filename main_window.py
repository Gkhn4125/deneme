"""
ui/main_window.py

Uygulamanın ana penceresini ve temel arayüz iskeletini oluşturur.
"""

import customtkinter as ctk

import config


class MainWindow(ctk.CTk):
    """Kitap Arşivim uygulamasının ana penceresi."""

    def __init__(self) -> None:
        super().__init__()

        self.setup_window()
        self.configure_grid()
        self.create_sidebar()
        self.create_book_list_panel()
        self.create_detail_panel()

    def setup_window(self) -> None:
        """Ana pencerenin temel ayarlarını yapar."""

        self.title(config.APP_NAME)

        self.geometry(
            f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}"
        )

        self.resizable(
            config.WINDOW_RESIZABLE,
            config.WINDOW_RESIZABLE
        )

    def configure_grid(self) -> None:
        """Ana pencerenin satır ve sütun yapılandırmasını yapar."""

        self.grid_rowconfigure(0, weight=1)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

    def create_sidebar(self) -> None:
        """Sol taraftaki menü panelini oluşturur."""

        sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0
        )

        sidebar.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        sidebar.grid_propagate(False)  # Sabit genişlik için grid propagasyonu kapatılır

        app_title = ctk.CTkLabel(
            sidebar,
            text="📚 Kitap Arşivi Uygulaması v1.0",
            font=("Segoe UI", 22, "bold")
        )

        app_title.grid(
            row=0,
            column=0,
            padx=20,
            pady=(30, 40)
        )

        new_book_button = ctk.CTkButton(
            sidebar,
            text="➕ Yeni Kitap"
        )

        new_book_button.grid(
            row=1,
            column=0,
            padx=20,
            pady=10,
            sticky="ew"
        )

        books_button = ctk.CTkButton(
            sidebar,
            text="📖 Kitaplar"
        )

        books_button.grid(
            row=2,
            column=0,
            padx=20,
            pady=10,
            sticky="ew"
        )

        statistics_button = ctk.CTkButton(
            sidebar,
            text="📊 İstatistikler"
        )

        statistics_button.grid(
            row=3,
            column=0,
            padx=20,
            pady=10,
            sticky="ew"
        )

        settings_button = ctk.CTkButton(
            sidebar,
            text="⚙️ Ayarlar"
        )

        settings_button.grid(
            row=4,
            column=0,
            padx=20,
            pady=10,
            sticky="ew"
        )

    def create_book_list_panel(self) -> None:
        """Orta bölümdeki kitap listesi panelini oluşturur."""

        book_list_panel = ctk.CTkFrame(self)

        book_list_panel.grid(
            row=0,
            column=1,
            padx=(20, 10),
            pady=20,
            sticky="nsew"
        )

        book_list_panel.grid_columnconfigure(0, weight=1)
        book_list_panel.grid_rowconfigure(2, weight=1)

        title_label = ctk.CTkLabel(
            book_list_panel,
            text="Kitaplarım",
            font=("Segoe UI", 24, "bold")
        )

        title_label.grid(
            row=0,
            column=0,
            padx=20,
            pady=(20, 10),
            sticky="w"
        )

        search_entry = ctk.CTkEntry(
            book_list_panel,
            placeholder_text="Kitap veya yazar ara..."
        )

        search_entry.grid(
            row=1,
            column=0,
            padx=20,
            pady=10,
            sticky="ew"
        )

        empty_label = ctk.CTkLabel(
            book_list_panel,
            text="Henüz kitap eklenmedi.",
            font=("Segoe UI", 16)
        )

        empty_label.grid(
            row=2,
            column=0,
            padx=20,
            pady=20
        )

    def create_detail_panel(self) -> None:
        """Sağ bölümdeki kitap detay panelini oluşturur."""

        detail_panel = ctk.CTkFrame(self)

        detail_panel.grid(
            row=0,
            column=2,
            padx=(10, 20),
            pady=20,
            sticky="nsew"
        )

        detail_panel.grid_columnconfigure(0, weight=1)

        detail_title = ctk.CTkLabel(
            detail_panel,
            text="Kitap Detayı",
            font=("Segoe UI", 24, "bold")
        )

        detail_title.grid(
            row=0,
            column=0,
            padx=20,
            pady=(20, 10)
        )

        cover_placeholder = ctk.CTkLabel(
            detail_panel,
            text="📕\n\nKapak Fotoğrafı",
            width=220,
            height=300,
            corner_radius=12,
            fg_color=("gray85", "gray20"),
            font=("Segoe UI", 18)
        )

        cover_placeholder.grid(
            row=1,
            column=0,
            padx=30,
            pady=20
        )

        information_label = ctk.CTkLabel(
            detail_panel,
            text=(
                "Bir kitap seçtiğinde\n"
                "kitabın bilgileri burada gösterilecek."
            ),
            font=("Segoe UI", 16),
            justify="center"
        )

        information_label.grid(
            row=2,
            column=0,
            padx=30,
            pady=20
        )
