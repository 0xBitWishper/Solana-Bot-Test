
# Telegram Bot untuk Solana

Bot Telegram ini memungkinkan pengguna untuk melakukan transaksi di jaringan **Solana** menggunakan wallet **Phantom** mereka. Bot ini menggunakan berbagai teknologi, termasuk **python-telegram-bot**, **Solana Python SDK**, dan **python-dotenv**.

## Pembuat
Script by **0xBitWishper**.

## Fitur
- Kirim token Solana (SOL) ke alamat yang ditentukan.
- Dapat digunakan dengan wallet **Phantom** untuk autentikasi dan transaksi.
- Memanfaatkan **Telegram Bot API** untuk komunikasi dengan pengguna.

## Instalasi

### Persyaratan
1. Python 3.8 atau lebih tinggi.
2. Akun Telegram dan token bot yang diperoleh melalui [BotFather](https://core.telegram.org/bots#botfather).
3. Keypair **Phantom Wallet** untuk mengakses jaringan Solana.

### Langkah-langkah Instalasi

1. **Clone repository ini:**

    ```bash
    git clone <URL_REPO>
    cd telegram-bot
    ```

2. **Buat lingkungan virtual:**

    ```bash
    python -m venv venv
    ```

3. **Aktifkan lingkungan virtual:**
    - Pada Windows:
      ```powershell
      .\venv\Scripts\Activate
      ```
    - Pada macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Instal dependensi yang diperlukan:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Buat file `.env` untuk menyimpan variabel lingkungan.** Contoh format file `.env`:

    ```bash
    TELEGRAM_API_TOKEN=your_telegram_api_token_here
    PRIVATE_KEY=your_private_key_here
    ```

6. **Jalankan bot:**

    ```bash
    python bot.py
    ```

### Daftar Dependensi
- **python-telegram-bot**: Wrapper untuk API Telegram Bot.
- **solana**: Library Python untuk berinteraksi dengan jaringan Solana.
- **python-dotenv**: Untuk mengelola variabel lingkungan dengan file `.env`.

## Penggunaan
Setelah bot aktif, Anda dapat mengirim perintah tertentu ke bot di Telegram, dan bot akan memprosesnya untuk melakukan transaksi Solana sesuai dengan fungsi yang telah dikodekan.

### Contoh Perintah:
- Kirim saldo Solana ke alamat lain.

## Kontribusi
Jika Anda ingin berkontribusi, Anda bisa membuka **pull request** atau membuat **issue** baru. Semua kontribusi sangat dihargai.

---

Terima kasih telah menggunakan proyek ini. Semoga bermanfaat!
