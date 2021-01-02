from command.createBotHandler import (createCommandHandler,
                                      createConversationHandler,
                                      createMessageHandler)
from command.createDiseaseHandler import createDiseaseHandler
from helpers.accesss_env import access_env
from telegram.ext import Updater

TOKEN = access_env("BOT_TOKEN") #get token from dotenv

updater = Updater(token=TOKEN, use_context=True) #create updater instance
dispatcher = updater.dispatcher

start_handler = createCommandHandler('start', 'start')

sendPhoto_handler = createCommandHandler('send_photo', 'sendPhoto')

sendUserPhoto_handler = createMessageHandler('send_user_photo', 'sendUserPhoto')

processPhoto_handler = createMessageHandler('process_photo', 'processPhoto')

# TODO: use mysqlite to store disease command name and description. Then loop over the dieases to create each disease handler.

keong_mas_handler = createDiseaseHandler(
    '1', "\
    +Pengertian Hama :\n\
Keong mas merupakan salah satu hama utama tanaman padi. Stadia rentan padi yaitu: persemaian dan padi 10 HST. Mekanisme merusak: keong memarut jaringan tanaman dan memakannya. Gejala kerusakan: tanaman muda dimakan hingga habis sehingga banyak rumpun hilang, satu batang padi akan habis dimakan seekor keong selama 3-5 menit.\n \
+Pengendalian secara kultur :\n\
Pada saat awal tanaman yaitu umur padi 0-25 hari, lahan sawah perlu dikeringkan dalam keadaan macak-macak hingga keong tidak dapat merayap menuju rumpun padi yang akan diserang. Kalaupun diserang, persentase serangan di bawah ambang kerusakan.\n\
Pembuatan parit di sekeliling lahan pertanaman agar keong dapat berkumpul lalu dimusnahkan.\n\
Saluran air perlu dibersihkan dari tanaman-tanaman air seperti kangkung dan lainnya agar tidak menjadi makanan cadangan bagi berkembangnya keong mas.\n\
+Induk keong dan kelompok telur yang tampak dilihat semuanya harus diambil dan dikumpulkan untuk dimusnahkan.\n\
Pasang saringan dari kawat di pintu air masuk ke lahan sawah sehingga keong dapat terjaring dan tertahan di kawat tersebut.\n\
Pasang ajir dari kayu untuk tempat meletakkan kelompok telur keong sehingga mudah diambil dan dibuang.\n\
Dalam parit yang dibuat diberi umpan perangkap berupa daun papaya atau kulit pisang sehingga keong tertarik dan berkumpul sehingga mudah diambil serta dimusnahkan."
    )

wereng_coklat_handler = createDiseaseHandler(
    '2', "\
+Pengertian Hama:\n\
Wereng coklat menyukai pertanaman yang dipupuk nitrogen tinggi dengan jarak tanam rapat. Ambang ekonomi hama ini adalah 15 ekor per rumpun. Siklus hidupnya 21-33 hari.\n\
Pengedalian :\n\
Cara pengendaliannya adalah sebagai berikut:\n \n\
Gunakan varietas tahan wereng coklat.\n\
Berikan pupuk K untuk mengurangi kerusakan.\n\
Monitor pertanaman paling lambat 2 minggu sekali.\n\
Bila populasi hama di bawah ambang ekonomi gunakan insektisida botani atau jamur entomopatogen (Metarhizium annisopliae atau Beauveria bassiana).\n\
Bila populasi hama di atas ambang ekonomi gunakan insektisida kimiawi yang direkomendasikan."
)

penggerek_batang_handler = createDiseaseHandler(
    '3', "\
Pengertian :\n\
Hama paling penting pada tanaman padi, sering menimbulkan kerusakan berat dan kehilangan hasil yang tinggi. Stadia tanaman yang rentan terhadap serangan penggerek batang adalah sejak pembibitan sampai pembentukan malai. Gejala kerusakan yang ditimbulkannya mengakibatkan anakan mati atau sering disebut sundep pada tanaman stadia vegetative dan beluk (malai hampa) pada tanaman stadia generative. Gejala sundep yaitu daun menguning, mengering, dan mati serta anakan kerdil. Sedangkan untuk gejala beluk yaitu malai padi berwarna coklat dan kering, gabah hampa, serta batang dicabut mudah terlepas\n\
Pengendalian:\n\
Tanam serempak.\n\
Pengumpulan kelompok telur.\n\
Aplikasi pestisida secara tepat.\n\
Spot treatment pada tanaman bergejala.\n\
Aplikasi agen hayati parasitoid telur (Trichogramma sp.)"
)

walang_sangit_handler = createDiseaseHandler(
    '4', "\
Walang sangit merupakan hama yang umum merusak bulir padi pada fase pemasakan, fase penumbuhan tanaman padi yang rentan terhadap serangan walang sangit adalah dari keluarnya malai sampai matang susu. Kerusakan yang ditimbulkannya menyebabkan beras berubah warna dan mengapung, serta hampa. Ambang ekonomi walang sangit adalah lebih dari satu ekor walang sangit per dua rumpun pada masa keluar malai sampai fase pembungaan.\n\n\
Cara pengendaliannya adalah:\n\n\
Kendalikan gulma di sawah dan di sekitar pertanaman.\n\
Pupuk lahan secara merata agar pertumbuhan tanaman seragam.\n\
Tangkap walang sangit dengan menggunakan jaring sebelum stadia pembungaan.\n\
Umpan walang sangit dengan menggunakan ikan yang sudah busuk, daging yang sudah rusak, atau dengan kotoran ayam.\n\
Apabila serangan sedang mencapai ambang ekonomi, lakukan penyemprotan insektisida.\n\
Lakukan penyemprotan pada pagi sekali atau sore hari ketika walang sangit berada di kanopi.\n\
Pengendalian hama walang sangit juga dapat dengan cara pemanfaatan keong mas. Cara membuat perangkap:\n\n\
Alat: botol bekas, pisai cutter, kawat, daging keong mas, lem perekat (bisa juga menggunakan air detergen), air, bamboo.\n\n\
Cara pembuatan:\n\n\
Lubangi dua sisi botol bekas.\n\
Lengkungkan bekas sayatan ke atas.\n\
Lubangi tutup botol untuk memasukkan kawat.\n\
Masukkan dan gantung 3-5 bangkai keong dengan memasukkannya ke kawat.\n\
Gunakan perekat atau cairan detergen.\n\
Jika dengan perekat, olesi dinding botol dengan lem.\n\
Jika dengan cairan detergen, masukkan air dan detergen ke dalam botol.\n\
Letakkan perangkap di dalam petakan sawah dengan menggunakan tiang bamboo."
)

hbd_atau_kresek_handler = createDiseaseHandler(
    '5', "\
Penyakit HDB atau Kresek disebabkan oleh bakteri Xanthomonas campestris pv oryzae. Gejala kresek dimulai dari tepi daun, berwarna keabu-abuan dan lama-lama daun menjadi kering. Bagian yang kering ini akan semakin meluas ke arah tulang daun hingga seluruh daun akan tampak mengering. Bila serangan terjadi saat berbunga, proses pengisian gabah menjadi tidak sempurna, menyebabkan gabah tidak terisi penuh atau bahkan hampa. Pada kondisi seperti ini kehilangan hasil bisa mencapai 50-70 persen.\n\n\
Prinsip pengendalian yang dapat dilakukan adalah:\n\n\
Penggunaan benih dan bibit sehat.\n\
Penggunaan agen hayati Corynebacterium atau Paenybacillus polymyxa pada benih umur 14, 28, dan 42 HST dengan dosis 5 cc per liter.\n\
Pemupukan berimbang, hindari pemupukan N berlebihan, sedangkan P dan K yang cukup.\n\
Hindari pemupukan saat tanaman memasuki fase bunting.\n\
Sanitasi lingkungan dan gulma inang.\n\
Pengairan berselang (satu hari digenangi, tiga hari dikeringkan)."
)

diseases = {
    0: [keong_mas_handler, wereng_coklat_handler, penggerek_batang_handler, walang_sangit_handler, hbd_atau_kresek_handler]
}

diseaseConversationFallback_handler = createCommandHandler('batal', 'cancelDiseaseConvo')

diseasesConversation_handler = createConversationHandler(start_command_name='mulai_percakapan_penyakit', start_function_name='startDiseaseConvo', context_command_list=diseases, fallbacks=[diseaseConversationFallback_handler], timeout=10)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(sendPhoto_handler)
dispatcher.add_handler(sendUserPhoto_handler)
dispatcher.add_handler(processPhoto_handler)
dispatcher.add_handler(diseasesConversation_handler)

if __name__ == '__main__':
    updater.start_polling()
