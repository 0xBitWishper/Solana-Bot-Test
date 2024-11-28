import os
from dotenv import load_dotenv
from solana.keypair import Keypair
from solana.rpc.api import Client
from base58 import b58decode
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Muat file .env
load_dotenv()

# Ambil PRIVATE_KEY dan TELEGRAM_TOKEN dari .env
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# Memastikan PRIVATE_KEY ada
if not PRIVATE_KEY:
    print("PRIVATE_KEY tidak ditemukan dalam file .env!")
    exit()

# Ubah PRIVATE_KEY (base58) menjadi Keypair Solana
try:
    private_key_bytes = b58decode(PRIVATE_KEY)  # Solana private key dalam base58
    keypair = Keypair.from_secret_key(private_key_bytes)
    print(f"Keypair berhasil dimuat. Public Key: {keypair.public_key}")
except Exception as e:
    print(f"Error dalam memuat private key: {e}")
    exit()

# Menghubungkan ke Solana Mainnet
solana_client = Client("https://api.mainnet-beta.solana.com")

# Fungsi untuk melihat saldo
def balance(update: Update, context: CallbackContext):
    # Ambil saldo akun
    balance = solana_client.get_balance(keypair.public_key)
    update.message.reply_text(f"Saldo Anda: {balance['result']['value']} lamports")

# Fungsi untuk mengirim SOL
def send_sol(update: Update, context: CallbackContext):
    if len(context.args) < 2:
        update.message.reply_text("Gunakan format: /send <alamat_tujuan> <jumlah_sol>")
        return

    # Ambil alamat tujuan dan jumlah SOL dari perintah
    recipient = context.args[0]
    amount = int(context.args[1])

    # Mempersiapkan transaksi
    try:
        transaction = solana_client.request_airdrop(keypair.public_key, amount)
        update.message.reply_text(f"Menunggu konfirmasi transaksi... {transaction}")
    except Exception as e:
        update.message.reply_text(f"Terjadi kesalahan: {e}")

# Fungsi utama untuk memulai bot
def main():
    # Inisialisasi Updater dengan token bot Telegram
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    
    # Mendapatkan dispatcher untuk mendaftarkan handler
    dp = updater.dispatcher

    # Menambahkan command handler
    dp.add_handler(CommandHandler("balance", balance))
    dp.add_handler(CommandHandler("send", send_sol))

    # Mulai bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
