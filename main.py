import pandas as pd
import random

def generate_travel_questions_and_answers():
    travel_data = []
    # Daftar kategori yang tersedia
    intents = [
        "wisata_alam", "wisata_budaya", "wisata_sejarah", "wisata_bahari", "wisata_rekreasi", "wisata_edukasi", "detail_wisata", "lokasi_wisata", "transportasi", "penginapan", "kuliner", "aktivitas", "budget", "cuaca"
    ]
    # 
    
    # Kategori dan pertanyaan yang sesuai dengan masing-masing kategori
    questions_dict = {
        "wisata_alam": [
            "Apa tempat wisata alam terbaik di [nama_daerah]?",
            "Di [nama_daerah], di mana saya bisa menikmati alam?",
            "Tempat wisata alam apa yang wajib dikunjungi di [nama_daerah]?",
            "Ada apa saja di [nama_daerah] yang cocok untuk pecinta alam?",
            "Wisata alam apa yang paling terkenal di [nama_daerah]?",
            "Apa saja tempat wisata alam di [nama_daerah] yang menawarkan pemandangan yang indah?",
            "Apa aja sih tempat wisata alam yang seru di [nama_daerah]?",
            "Lagi pengen healing nih, ada rekomendasi tempat alam di [nama_daerah]?",
            "Kalau mau nikmatin alam di [nama_daerah], enaknya ke mana ya?",
            "Tempat buat refreshing di alam sekitar [nama_daerah] ada nggak?",
            "Wisata alam yang asik di [nama_daerah] apa aja ya?",
            "Pengen liburan ke tempat yang hijau dan adem di [nama_daerah], saran dong!",
            "Kalau suka jalan-jalan ke alam terbuka, di [nama_daerah] ke mana aja?",
            "Ada tempat wisata alam yang cocok buat keluarga di [nama_daerah]?",
            "Tempat alam yang tenang dan nggak terlalu rame di [nama_daerah] ada nggak?",
            "Butuh rekomendasi wisata alam buat akhir pekan di sekitar [nama_daerah] dong!"
        ],
        "wisata_budaya": [
            "Tempat wisata budaya apa yang terkenal di [nama_daerah]?",
            "Apa yang bisa saya pelajari tentang budaya di [nama_daerah]?",
            "Di [nama_daerah], ada situs budaya yang menarik untuk dikunjungi?",
            "Adakah festival budaya yang diadakan di [nama_daerah]?",
            "Bagaimana sejarah budaya di [nama_daerah]?",
            "Apa saja museum budaya yang bisa saya kunjungi di [nama_daerah]?",
            "Di [nama_daerah], ada tempat yang memperkenalkan seni tradisional lokal?",
            "Apa yang membuat budaya di [nama_daerah] unik dan berbeda?",
            "Adakah pertunjukan seni budaya di [nama_daerah] yang bisa saya saksikan?",
            "Bagaimana cara menikmati pengalaman budaya di [nama_daerah]?"
        ],
        "wisata_sejarah": [
            "Apa tempat wisata sejarah yang ada di [nama_daerah]?",
            "Di [nama_daerah], apa yang bisa dipelajari tentang sejarah?",
            "Apa yang menarik tentang sejarah di [nama_daerah]?",
            "Tempat bersejarah apa yang wajib saya kunjungi di [nama_daerah]?",
            "Ada museum sejarah di [nama_daerah]?",
            "Apa situs bersejarah yang paling terkenal di [nama_daerah]?",
            "Di [nama_daerah], ada bangunan bersejarah yang bisa saya kunjungi?",
            "Adakah peninggalan sejarah yang terkenal di [nama_daerah]?",
            "Bagaimana pengaruh sejarah [nama_daerah] terhadap budaya lokal?",
            "Tempat sejarah mana yang menyimpan cerita penting bagi [nama_daerah]?"
        ],
        "wisata_bahari": [
            "Apa tempat wisata bahari yang paling terkenal di [nama_daerah]?",
            "Di [nama_daerah], di mana saya bisa snorkeling?",
            "Tempat wisata bahari apa yang cocok untuk liburan keluarga?",
            "Apa pantai terbaik untuk diving di [nama_daerah]?",
            "Di [nama_daerah], ada spot wisata bahari yang terkenal?",
            "Apa saja aktivitas bahari yang bisa dilakukan di [nama_daerah]?",
            "Di [nama_daerah], apakah ada tempat yang bagus untuk berselancar?",
            "Di mana saya bisa menikmati keindahan bawah laut di [nama_daerah]?",
            "Tempat wisata bahari mana yang paling direkomendasikan di [nama_daerah]?",
            "Bagaimana cara menuju spot diving terbaik di [nama_daerah]?"
        ],
        "wisata_rekreasi": [
            "Tempat wisata rekreasi apa yang cocok untuk anak-anak di [nama_daerah]?",
            "Di [nama_daerah], ada taman hiburan yang bisa saya kunjungi?",
            "Apa saja tempat wisata rekreasi di [nama_daerah] untuk keluarga?",
            "Apa aktivitas rekreasi yang bisa dilakukan di [nama_daerah]?",
            "Di [nama_daerah], ada tempat wisata rekreasi yang bisa dinikmati oleh semua usia?",
            "Tempat rekreasi mana yang terbaik untuk liburan keluarga di [nama_daerah]?",
            "Apa saja wahana menarik di taman hiburan [nama_daerah]?",
            "Di [nama_daerah], ada fasilitas rekreasi outdoor yang menarik?",
            "Bagaimana cara menuju tempat rekreasi terbaik di [nama_daerah]?",
            "Apa yang membedakan tempat wisata rekreasi di [nama_daerah] dengan tempat lainnya?"
        ],
        "wisata_edukasi": [
            "Apa saja tempat wisata edukasi yang menarik di [nama_daerah]?",
            "Di [nama_daerah], di mana saya bisa belajar sambil berwisata?",
            "Tempat wisata edukasi apa yang cocok untuk anak-anak di [nama_daerah]?",
            "Apa museum terbaik di [nama_daerah] untuk belajar sejarah?",
            "Di [nama_daerah], ada tempat yang cocok untuk belajar tentang alam?",
            "Di [nama_daerah], ada tempat wisata edukasi yang mengajarkan seni dan budaya?",
            "Apa yang bisa saya pelajari di tempat wisata edukasi di [nama_daerah]?",
            "Adakah wisata edukasi tentang sejarah di [nama_daerah]?",
            "Di [nama_daerah], apa tempat yang cocok untuk belajar tentang teknologi?",
            "Tempat wisata edukasi apa yang cocok untuk pelajar di [nama_daerah]?"
        ],
        "detail_wisata": [
            "Apa yang bisa saya pelajari tentang [nama_wisata]?",
            "Ceritakan lebih lanjut tentang [nama_wisata].",
            "Apa yang membuat [nama_wisata] unik?",
            "Di [nama_wisata], ada aktivitas apa saja yang bisa saya lakukan?",
            "Bagaimana sejarah dari [nama_wisata]?",
            "Apa yang membuat [nama_wisata] menjadi tempat yang wajib dikunjungi?",
            "Apa yang membedakan [nama_wisata] dengan tempat wisata lainnya?",
            "Dapatkah Anda memberi tahu saya lebih banyak tentang [nama_wisata]?",
            "Apa saja hal menarik yang bisa ditemukan di [nama_wisata]?",
            "Apa yang harus diketahui pengunjung sebelum pergi ke [nama_wisata]?"
        ],
        "lokasi_wisata": [
            "Di mana lokasi [nama_wisata]?",
            "Apa alamat lengkap dari [nama_wisata]?",
            "Di [nama_wisata], di kota dan provinsi mana saya dapat menemukannya?",
            "Bisa beri tahu saya alamat [nama_wisata]?",
            "Di [nama_wisata], di mana tempatnya berada?",
            "Alamat lengkap [nama_wisata] di mana?",
            "Apa kota dan provinsi yang meliputi [nama_wisata]?",
            "Di [nama_wisata], di bagian mana saya bisa menemukannya?",
            "Di [nama_wisata], apa alamat lengkap dan kota tempat wisata ini berada?",
            "Dimana saya bisa menemukan [nama_wisata]?"
        ],
        "transportasi": [
            "Bagaimana cara menuju ke [nama_daerah] dari [kota_asal]?",
            "Ada taksi atau transportasi umum yang bisa digunakan di [nama_daerah]?",
            "Bagaimana sistem transportasi di [nama_daerah]?",
            "Apakah di [nama_daerah] ada transportasi publik yang murah?",
            "Bagaimana cara menuju ke [rekomendasi_1] dari pusat kota?"
        ],
        "penginapan": [
            "Di [nama_daerah], ada hotel murah yang bagus?",
            "Apa hotel terbaik di [nama_daerah]?",
            "Di [nama_daerah], apakah ada penginapan yang cocok untuk backpacker?",
            "Bagaimana mencari tempat tinggal di [nama_daerah] untuk liburan panjang?",
            "Apa rekomendasi hotel bintang lima di [nama_daerah]?"
        ],
        "kuliner": [
            "Makanan khas [nama_daerah] apa yang harus saya coba?",
            "Apa restoran terbaik di [nama_daerah] untuk makan malam?",
            "Di [nama_daerah], ada warung makan enak yang bisa saya coba?",
            "Bagaimana dengan street food di [nama_daerah]?",
            "Apa saja makanan populer di [nama_daerah]?"
        ],
        "aktivitas": [
            "Apa aktivitas seru yang bisa saya lakukan di [nama_daerah]?",
            "Di [nama_daerah], ada aktivitas outdoor yang bisa saya coba?",
            "Apa yang bisa saya lakukan di [nama_daerah] selain wisata?",
            "Adakah tempat untuk berbelanja di [nama_daerah]?",
            "Apa aktivitas petualangan yang bisa saya coba di [nama_daerah]?"
        ],
        "budget": [
            "Berapa biaya rata-rata untuk liburan di [nama_daerah]?",
            "Apakah [nama_daerah] tempat yang mahal untuk wisata?",
            "Apa yang harus dipersiapkan untuk liburan dengan budget terbatas di [nama_daerah]?",
            "Berapa harga rata-rata penginapan di [nama_daerah]?",
            "Di [nama_daerah], berapa biaya makan sehari?"
        ],
        "cuaca": [
            "Bagaimana cuaca di [nama_daerah] bulan ini?",
            "Apakah di [nama_daerah] sering hujan?",
            "Bagaimana suhu rata-rata di [nama_daerah] saat musim kemarau?",
            "Cuaca seperti apa yang bisa saya harapkan di [nama_daerah] selama musim hujan?",
            "Apakah ada musim panas di [nama_daerah]?"
        ]
    }
    
    answers_dict = {
        "wisata_alam": [
            "Di [nama_daerah], kamu bisa nemuin banyak tempat wisata alam keren kayak [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Semuanya punya daya tarik alam yang bikin betah!",
            "Kalau kamu lagi di [nama_daerah] dan pengen menikmati alam, langsung aja ke [rekomendasi_1], [rekomendasi_2], atau [rekomendasi_3]. Cocok buat healing dan nyari udara segar.",
            "Beberapa destinasi wisata alam yang wajib kamu kunjungi di [nama_daerah] itu ada [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Pemandangannya cakep-cakep semua!",
            "Buat pecinta alam, [nama_daerah] punya banyak spot menarik kayak [rekomendasi_1] dan [rekomendasi_2]. Tempat-tempat ini sering jadi tujuan favorit buat yang suka suasana alam terbuka.",
            "[rekomendasi_1] dan [rekomendasi_2] adalah wisata alam yang paling terkenal di [nama_daerah]. Banyak orang datang ke sana buat nikmatin keindahan alam dan suasana yang tenang.",
            "Kalau cari pemandangan indah di [nama_daerah], kamu bisa mampir ke [rekomendasi_1], [rekomendasi_2], atau [rekomendasi_3]. Cocok banget buat yang suka foto-foto alam atau sekadar jalan santai.",
            "Kamu bisa coba ke [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Semuanya punya suasana alam yang bikin rileks.",
            "Di [nama_daerah] ada beberapa tempat keren buat healing, kayak [rekomendasi_1] sama [rekomendasi_2]. Kalau mau yang agak sepi, coba juga [rekomendasi_3].",
            "Coba deh mampir ke [rekomendasi_1], [rekomendasi_2], atau [rekomendasi_3]. View-nya bagus dan cocok buat refreshing.",
            "Kalau pengen dekat sama alam, [rekomendasi_1] sama [rekomendasi_2] bisa jadi pilihan. [rekomendasi_3] juga oke banget, lho.",
            "Di [nama_daerah] banyak pilihan, nih! [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3] wajib kamu kunjungi kalau suka alam.",
            "Buat yang pengen suasana hijau dan adem, coba deh ke [rekomendasi_1], terus lanjut ke [rekomendasi_2] dan [rekomendasi_3].",
            "Kalau kamu suka jalan-jalan di alam terbuka, [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3] bisa banget masuk list kamu.",
            "Buat liburan bareng keluarga, coba deh ke [rekomendasi_1], [rekomendasi_2], atau [rekomendasi_3]. Tempatnya enak buat santai.",
            "Kalau nyari tempat yang tenang, coba cek [rekomendasi_1] atau [rekomendasi_2]. Biasanya nggak terlalu rame dan adem.",
            "Buat akhir pekan, [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3] cocok banget buat ngilangin penat!"
        ],
        "wisata_budaya": [
            "Di [nama_daerah], Anda bisa mengunjungi [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3] untuk menjelajahi keindahan budaya yang unik. Jangan lewatkan juga [rekomendasi_4] yang kaya akan sejarah budaya lokal.",
            "Di [nama_daerah], budaya sangat kental dan Anda dapat mengunjungi tempat-tempat seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3] untuk melihat berbagai tradisi dan seni yang memukau.",
            "Tempat wisata budaya terbaik di [nama_daerah] termasuk [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang akan memberi Anda gambaran tentang sejarah dan warisan budaya setempat.",
            "Jika Anda tertarik dengan budaya, Anda bisa mengunjungi [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3] di [nama_daerah], yang penuh dengan nilai sejarah dan tradisi yang hidup hingga saat ini.",
            "Di [nama_daerah], Anda bisa menyaksikan beragam festival budaya seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang menunjukkan kekayaan seni dan tradisi lokal.",
            "Jika ingin mempelajari lebih dalam tentang budaya [nama_daerah], kunjungi [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang terkenal dengan situs-situs bersejarah dan karya seni yang luar biasa.",
            "Untuk menikmati budaya [nama_daerah], Anda bisa mengunjungi [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang menyajikan seni tradisional dan situs budaya yang kaya akan sejarah.",
            "Ada banyak tempat budaya di [nama_daerah], termasuk [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang menawarkan wawasan mendalam tentang kehidupan dan tradisi masyarakat lokal.",
            "Di [nama_daerah], Anda dapat menemukan banyak situs budaya menarik seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang memperkenalkan budaya tradisional serta keindahan seni lokal.",
            "Di [nama_daerah], Anda bisa menikmati festival budaya yang sangat terkenal, seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang merayakan seni, musik, dan tarian tradisional."
        ],
        "wisata_sejarah": [
            "Di [nama_daerah], Anda bisa mengunjungi [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang terkenal dengan situs sejarah yang luar biasa. Jangan lewatkan [rekomendasi_4] yang sarat dengan cerita masa lalu.",
            "Tempat wisata sejarah terbaik di [nama_daerah] antara lain [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Tempat-tempat ini memiliki nilai sejarah yang sangat tinggi dan layak dikunjungi.",
            "Untuk mempelajari sejarah di [nama_daerah], kunjungi [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang menawarkan pengalaman belajar yang mendalam tentang budaya dan masa lalu daerah ini.",
            "Di [nama_daerah], Anda bisa menikmati sejarah melalui kunjungan ke [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Setiap tempat ini penuh dengan cerita dan peninggalan yang menarik.",
            "Beberapa tempat wisata sejarah di [nama_daerah] yang wajib dikunjungi adalah [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Setiap tempat memberikan wawasan unik tentang masa lalu.",
            "Jika Anda tertarik dengan sejarah, jangan lewatkan untuk mengunjungi [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3] di [nama_daerah]. Anda akan belajar banyak tentang sejarah dan budaya lokal.",
            "Tempat bersejarah yang terkenal di [nama_daerah] meliputi [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Di sini, Anda dapat menjelajahi sejarah yang menarik dan warisan budaya yang kaya.",
            "Sejarah [nama_daerah] dapat ditemukan di tempat-tempat seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang menawarkan kisah-kisah masa lalu yang menginspirasi.",
            "Beberapa situs sejarah di [nama_daerah] yang wajib Anda kunjungi antara lain [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Setiap tempat memiliki keunikan sejarah yang tak terlupakan.",
            "Untuk menyelami lebih dalam tentang sejarah [nama_daerah], Anda bisa mengunjungi [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang penuh dengan peninggalan sejarah yang memukau."
        ],
        "wisata_bahari": [
            "Di [nama_daerah], Anda bisa menikmati keindahan laut di [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang terkenal dengan pantai yang indah dan kegiatan snorkeling yang seru.",
            "Pantai-pantai terbaik untuk diving di [nama_daerah] termasuk [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang menawarkan pemandangan bawah laut yang memukau.",
            "Di [nama_daerah], Anda bisa menjelajahi keindahan bawah laut di [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Snorkeling dan diving di sini sangat direkomendasikan!",
            "Untuk liburan bahari yang sempurna, Anda bisa mengunjungi [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3] di [nama_daerah], yang terkenal dengan keindahan pantainya.",
            "Tempat wisata bahari terbaik di [nama_daerah] antara lain [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Anda dapat menikmati berbagai aktivitas seperti snorkeling, diving, atau sekadar bersantai di pantai.",
            "Di [nama_daerah], Anda bisa menikmati berbagai aktivitas bahari di pantai-pantai seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Jangan lewatkan kesempatan untuk diving atau snorkeling di sana.",
            "Pantai di [nama_daerah] seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3] adalah tempat yang tepat untuk liburan bahari. Nikmati keindahan alam laut dan berbagai kegiatan menarik lainnya.",
            "Jika Anda suka beraktivitas di laut, [nama_daerah] memiliki banyak tempat wisata bahari seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3] yang cocok untuk liburan yang penuh petualangan.",
            "Tempat wisata bahari yang terkenal di [nama_daerah] antara lain [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Nikmati kegiatan seperti snorkeling atau sekadar bersantai di pantai yang indah.",
            "Pantai di [nama_daerah] yang populer untuk kegiatan bahari termasuk [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Jangan lupa membawa perlengkapan diving atau snorkeling!"
        ],
        "wisata_rekreasi": [
            "Di [nama_daerah], Anda bisa mengunjungi tempat rekreasi seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3] yang cocok untuk anak-anak dan keluarga.",
            "Tempat wisata rekreasi di [nama_daerah] yang ideal untuk keluarga antara lain [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Nikmati berbagai aktivitas seru bersama anak-anak.",
            "Di [nama_daerah], Anda bisa mengunjungi [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang sangat cocok untuk keluarga yang ingin bersenang-senang di luar ruangan.",
            "Jika Anda mencari tempat rekreasi untuk keluarga di [nama_daerah], cobalah mengunjungi [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang menawarkan banyak aktivitas menyenangkan.",
            "Untuk liburan rekreasi keluarga, Anda bisa mengunjungi [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3] di [nama_daerah], yang memiliki wahana dan fasilitas hiburan yang cocok untuk anak-anak.",
            "Di [nama_daerah], banyak tempat rekreasi yang cocok untuk anak-anak dan keluarga, seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Nikmati berbagai permainan dan atraksi.",
            "Tempat wisata rekreasi terbaik di [nama_daerah] antara lain [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Ini adalah pilihan tepat untuk liburan seru bersama keluarga.",
            "Jika Anda ingin liburan rekreasi di [nama_daerah], Anda bisa mengunjungi [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang menyediakan berbagai kegiatan menarik untuk semua usia.",
            "Di [nama_daerah], Anda bisa menikmati rekreasi keluarga di tempat-tempat seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Ini adalah tempat yang ideal untuk anak-anak dan orang dewasa.",
            "Untuk rekreasi keluarga di [nama_daerah], Anda bisa mengunjungi [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Tempat-tempat ini menawarkan wahana seru dan area bermain untuk anak-anak."
        ],
        "wisata_edukasi": [
            "Di [nama_daerah], Anda bisa mengunjungi [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3] untuk pengalaman wisata edukasi yang luar biasa. Setiap tempat menawarkan wawasan baru tentang sejarah, budaya, atau alam.",
            "Beberapa tempat wisata edukasi terbaik di [nama_daerah] adalah [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang menawarkan pengalaman belajar yang menyenangkan dan menarik untuk semua usia.",
            "Untuk pengalaman wisata edukasi di [nama_daerah], Anda bisa mengunjungi [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Di sana, Anda bisa mempelajari lebih dalam tentang sejarah, seni, dan alam.",
            "Jika Anda ingin belajar sambil berwisata, coba kunjungi [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3] di [nama_daerah]. Tempat-tempat ini menawarkan berbagai pengalaman edukatif yang menyenangkan.",
            "Di [nama_daerah], Anda bisa menemukan berbagai museum dan pusat edukasi seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang cocok untuk mempelajari seni, sejarah, dan budaya.",
            "Untuk anak-anak, [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3] adalah tempat wisata edukasi yang menggabungkan kesenangan dan pembelajaran dalam satu paket.",
            "Di [nama_daerah], Anda bisa belajar lebih banyak tentang alam dan ekosistem melalui tempat-tempat seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang menawarkan pengalaman interaktif dan edukatif.",
            "Jika Anda tertarik untuk mempelajari seni dan budaya, cobalah mengunjungi [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3] di [nama_daerah]. Tempat-tempat ini akan memberikan wawasan mendalam tentang warisan budaya lokal.",
            "Ada banyak tempat wisata edukasi di [nama_daerah] yang dapat mengajarkan Anda tentang sejarah dan ilmu pengetahuan, seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3].",
            "Jika Anda ingin mengeksplorasi teknologi dan inovasi, [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3] di [nama_daerah] menawarkan pameran dan kegiatan yang berfokus pada dunia teknologi dan ilmu pengetahuan."
        ],
        "detail_wisata": [
            "Di [nama_wisata], Anda bisa menikmati [description].",
            "Tempat ini terkenal karena [description].",
            "Sejarah [nama_wisata] sangat menarik, [description].",
            "Di [nama_wisata], Anda bisa melakukan [description].",
            "[nama_wisata] dikenal dengan [description].",
            "Tempat ini menawarkan [description] yang unik.",
            "Anda bisa belajar banyak tentang [description] di [nama_wisata].",
            "[nama_wisata] memiliki [description] yang luar biasa.",
            "Jika Anda mengunjungi [nama_wisata], Anda akan menemukan [description].",
            "Pengunjung di [nama_wisata] dapat menikmati [description]."
        ],
        "lokasi_wisata": [
            "[nama_wisata] terletak di [alamat], [nama_kota_kabupaten], [nama_provinsi]. Tempat ini dikenal dengan [deskripsi].",
            "Anda bisa mengunjungi [nama_wisata] di [alamat], [nama_kota_kabupaten], [nama_provinsi]. [deskripsi]",
            "Alamat [nama_wisata] adalah [alamat], yang berada di [nama_kota_kabupaten], [nama_provinsi]. [deskripsi]",
            "[nama_wisata] dapat ditemukan di [alamat], [nama_kota_kabupaten], [nama_provinsi]. [deskripsi]",
            "[nama_wisata] berlokasi di [alamat], [nama_kota_kabupaten], [nama_provinsi]. Tempat ini terkenal dengan [deskripsi].",
            "Untuk menemukan [nama_wisata], datanglah ke [alamat], [nama_kota_kabupaten], [nama_provinsi]. Di sana, Anda akan menemukan [deskripsi].",
            "[nama_wisata] berada di [alamat], [nama_kota_kabupaten], [nama_provinsi]. Ini adalah tempat yang sangat menarik karena [deskripsi].",
            "[nama_wisata] terletak di [alamat], di [nama_kota_kabupaten], [nama_provinsi]. Di tempat ini, Anda bisa menemukan [deskripsi].",
            "[nama_wisata] terletak di [alamat], [nama_kota_kabupaten], [nama_provinsi]. Destinasi ini terkenal karena [deskripsi].",
            "Jika Anda ingin mengunjungi [nama_wisata], datanglah ke [alamat], [nama_kota_kabupaten], [nama_provinsi]. Tempat ini menawarkan [deskripsi]."
        ],
        "transportasi": [
            "Untuk menuju ke [nama_daerah] dari [kota_asal], Anda bisa naik pesawat, kereta, atau bus. Setibanya di sana, Anda bisa menggunakan taksi atau transportasi umum seperti bus dan ojek online.",
            "Sistem transportasi di [nama_daerah] sangat terjangkau, dengan banyak pilihan seperti taksi, bus, dan ojek online. Anda dapat dengan mudah menggunakan transportasi umum untuk berkeliling.",
            "Di [nama_daerah], Anda bisa menggunakan taksi atau bus untuk berkeliling. Transportasi umum seperti angkutan kota dan ojek online juga tersedia di banyak area.",
            "Untuk pergi ke [nama_daerah], Anda bisa menggunakan penerbangan langsung dari [kota_asal], atau naik kereta dan melanjutkan dengan bus atau taksi setibanya di sana.",
            "Di [nama_daerah], transportasi publik cukup mudah diakses. Anda dapat menggunakan bus, taksi, atau layanan ojek online yang banyak tersedia untuk bepergian ke tempat wisata.",
            "Dari [kota_asal], Anda bisa terbang langsung ke [nama_daerah] dan melanjutkan perjalanan dengan taksi atau transportasi umum setibanya di sana.",
            "Transportasi umum di [nama_daerah] termasuk bus, taksi, dan ojek online. Jika Anda ingin lebih fleksibel, Anda juga bisa menyewa mobil atau motor.",
            "Di [nama_daerah], transportasi publik seperti bus dan taksi tersedia di hampir setiap sudut kota. Anda juga bisa menggunakan ojek online untuk perjalanan yang lebih cepat.",
            "Untuk menuju ke [nama_daerah] dari [kota_asal], Anda dapat menggunakan penerbangan langsung atau naik bus jarak jauh. Di [nama_daerah], Anda bisa menggunakan taksi atau angkutan umum lainnya.",
            "Jika Anda berada di [nama_daerah], Anda bisa menggunakan transportasi umum seperti bus dan taksi untuk berkeliling. Ojek online juga merupakan pilihan yang praktis dan cepat."
        ],
        "penginapan": [
            "Di [nama_daerah], Anda bisa menginap di penginapan yang terjangkau seperti [rekomendasi_1], [rekomendasi_2], atau [rekomendasi_3]. Untuk pengalaman lebih mewah, coba [rekomendasi_4].",
            "Untuk penginapan mewah di [nama_daerah], Anda bisa memilih hotel seperti [rekomendasi_1], [rekomendasi_2], atau [rekomendasi_3]. Hotel-hotel ini menawarkan kenyamanan dan fasilitas bintang lima.",
            "Jika Anda seorang backpacker, penginapan yang terjangkau seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3] di [nama_daerah] bisa menjadi pilihan yang sempurna.",
            "Di [nama_daerah], Anda dapat memilih penginapan yang cocok dengan anggaran Anda, seperti [rekomendasi_1], [rekomendasi_2], atau [rekomendasi_3] yang menawarkan harga terjangkau.",
            "Untuk liburan yang lebih mewah, Anda bisa memilih hotel-hotel bintang lima di [nama_daerah] seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3].",
            "Bagi wisatawan dengan anggaran terbatas, ada banyak pilihan penginapan murah di [nama_daerah], seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3].",
            "Jika Anda mencari penginapan dengan pemandangan indah, cobalah [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3] yang menawarkan fasilitas yang nyaman dan lokasi strategis.",
            "Di [nama_daerah], Anda bisa menginap di berbagai hotel dan penginapan, seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang menyediakan fasilitas lengkap dan layanan ramah.",
            "Bagi yang suka berkemah, di [nama_daerah] ada tempat-tempat penginapan yang menawarkan pengalaman menginap dekat alam, seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3].",
            "Di [nama_daerah], Anda bisa memilih penginapan seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3] yang menyediakan berbagai fasilitas mulai dari kamar sederhana hingga hotel mewah."
        ],
        "kuliner": [
            "Makanan khas [nama_daerah] yang harus Anda coba adalah [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Jangan lewatkan juga [rekomendasi_4] yang sangat populer di kalangan wisatawan.",
            "Di [nama_daerah], Anda wajib mencoba makanan khas seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Jangan lupa untuk mencicipi juga [rekomendasi_4] yang terkenal di sini.",
            "Beberapa makanan khas yang populer di [nama_daerah] termasuk [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Ini adalah hidangan yang wajib dicoba oleh setiap pengunjung.",
            "Di [nama_daerah], Anda bisa mencoba makanan lokal yang khas seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang menggugah selera dengan rasa otentik.",
            "Jika Anda berada di [nama_daerah], pastikan untuk mencoba [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang menawarkan cita rasa yang berbeda dari makanan lainnya.",
            "Makanan jalanan di [nama_daerah] sangat lezat, seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Cobalah [rekomendasi_4] yang sangat disukai oleh penduduk lokal.",
            "Di [nama_daerah], makanan khas yang harus dicicipi adalah [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Anda juga bisa mencoba [rekomendasi_4] yang tak kalah enaknya.",
            "Jika Anda penggemar kuliner, [nama_daerah] menawarkan berbagai pilihan makanan enak seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3].",
            "Di [nama_daerah], Anda bisa menemukan berbagai restoran yang menyajikan [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang patut dicoba saat berkunjung.",
            "Jangan lupa untuk mencoba [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3] saat Anda berada di [nama_daerah]. Ini adalah beberapa makanan favorit yang sering dicari wisatawan."
        ],
        "aktivitas": [
            "Di [nama_daerah], Anda bisa menikmati aktivitas seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Ini adalah pilihan terbaik untuk petualangan atau liburan santai.",
            "Aktivitas yang bisa Anda coba di [nama_daerah] termasuk [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang sangat cocok untuk wisatawan yang mencari tantangan.",
            "Di [nama_daerah], Anda bisa mencoba berbagai aktivitas seru seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang cocok untuk semua usia.",
            "Bagi pencinta alam, [nama_daerah] memiliki banyak aktivitas outdoor seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Jangan lupa untuk mencoba [rekomendasi_4] yang menyenangkan.",
            "Jika Anda mencari aktivitas seru, Anda bisa mencoba [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3] di [nama_daerah]. Ada banyak pilihan aktivitas outdoor yang menantang!",
            "Di [nama_daerah], Anda bisa menikmati berbagai aktivitas menarik seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3], yang memberikan pengalaman baru dan menyenangkan.",
            "Jika Anda mencari kegiatan untuk keluarga, Anda bisa mencoba [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3] di [nama_daerah]. Tempat-tempat ini cocok untuk liburan keluarga.",
            "Ada banyak aktivitas yang bisa Anda coba di [nama_daerah], seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Setiap aktivitas memberikan pengalaman unik yang tak terlupakan.",
            "Untuk liburan yang lebih seru, coba lakukan aktivitas seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3]. Ini adalah aktivitas yang sangat populer di [nama_daerah].",
            "Di [nama_daerah], Anda bisa mencoba aktivitas seperti [rekomendasi_1], [rekomendasi_2], dan [rekomendasi_3] yang menggabungkan alam dan petualangan."
        ],
        "budget": [
            "Untuk liburan di [nama_daerah], Anda bisa memperkirakan biaya sekitar [rekomendasi_1] untuk penginapan dan [rekomendasi_2] untuk makan sehari.",
            "Di [nama_daerah], biaya liburan bisa bervariasi. Untuk penginapan, Anda bisa menganggarkan sekitar [rekomendasi_1], sementara biaya makan sekitar [rekomendasi_2].",
            "Jika Anda bepergian dengan anggaran terbatas, perkirakan biaya sekitar [rekomendasi_1] untuk penginapan murah dan [rekomendasi_2] untuk makan sehari di [nama_daerah].",
            "Berapa biaya rata-rata di [nama_daerah]? Biaya penginapan biasanya sekitar [rekomendasi_1] dan makan sekitar [rekomendasi_2] per hari.",
            "Untuk liburan dengan budget terbatas di [nama_daerah], Anda bisa memperkirakan biaya sekitar [rekomendasi_1] untuk penginapan dan [rekomendasi_2] untuk makanan sehari.",
            "Biaya liburan di [nama_daerah] bisa lebih murah jika Anda memilih penginapan yang lebih sederhana. Anggarkan sekitar [rekomendasi_1] untuk penginapan dan [rekomendasi_2] untuk makan sehari.",
            "Jika Anda ingin liburan hemat, [nama_daerah] menawarkan pilihan penginapan murah dengan biaya sekitar [rekomendasi_1] per malam, serta makan seharga [rekomendasi_2] per hari.",
            "Untuk liburan di [nama_daerah] dengan anggaran terbatas, Anda bisa memilih penginapan dengan harga sekitar [rekomendasi_1] dan makan dengan biaya sekitar [rekomendasi_2].",
            "Biaya liburan di [nama_daerah] relatif terjangkau, dengan penginapan di kisaran harga [rekomendasi_1] dan makan sekitar [rekomendasi_2] sehari.",
            "Anggaran untuk liburan di [nama_daerah] bisa dimulai dari sekitar [rekomendasi_1] untuk penginapan dan [rekomendasi_2] untuk makanan sehari."
        ],
        "cuaca": [
            "Cuaca di [nama_daerah] bulan ini biasanya [cuaca]. Suhu rata-rata berkisar antara [suhu_min] dan [suhu_max] derajat Celsius, jadi pastikan untuk mempersiapkan pakaian yang sesuai.",
            "Di [nama_daerah], cuaca cenderung [cuaca] bulan ini. Pada musim hujan, curah hujan bisa meningkat, jadi pastikan untuk membawa payung atau jas hujan.",
            "Selama musim kemarau, suhu di [nama_daerah] bisa mencapai [suhu_max] derajat Celsius, dengan cuaca yang [cuaca]. Anda bisa mengharapkan cuaca cerah dan kering.",
            "Pada bulan ini, cuaca di [nama_daerah] biasanya [cuaca]. Suhu rata-rata sekitar [suhu_min] hingga [suhu_max] derajat Celsius, cocok untuk kegiatan luar ruangan.",
            "Cuaca di [nama_daerah] bulan ini cukup [cuaca]. Pada musim hujan, Anda dapat mengharapkan hujan ringan hingga sedang, jadi pastikan untuk membawa payung.",
            "Jika Anda berencana berkunjung ke [nama_daerah] pada bulan ini, cuaca umumnya [cuaca]. Musim hujan dimulai pada bulan [bulan_hujan], dengan suhu rata-rata sekitar [suhu_min].",
            "Cuaca di [nama_daerah] pada musim kemarau cukup panas dengan suhu rata-rata sekitar [suhu_max] derajat Celsius, dengan langit cerah dan sedikit hujan.",
            "Selama musim hujan di [nama_daerah], Anda akan mengalami cuaca [cuaca] dengan curah hujan tinggi, terutama pada sore hari. Suhu biasanya berada di kisaran [suhu_min] hingga [suhu_max] derajat Celsius.",
            "Cuaca di [nama_daerah] saat musim panas cenderung [cuaca], dengan suhu yang bisa mencapai [suhu_max] derajat Celsius. Ini adalah waktu yang tepat untuk menikmati aktivitas outdoor.",
            "Cuaca di [nama_daerah] pada musim hujan dapat sangat [cuaca], dengan suhu sekitar [suhu_min] hingga [suhu_max] derajat Celsius. Jangan lupa bawa perlengkapan hujan."
        ]
    }
    
    for intent in intents:
        questions = questions_dict.get(intent, [])
        answers = answers_dict.get(intent, [])
        
        for i, question in enumerate(questions):
            if i < len(answers):  # cek jika answer tersedia
                answer = answers[i]
            else:
                answer = ""  # fallback jika tidak ada jawaban
            
            travel_data.append((question, intent, answer))

    
    return travel_data

# Menghasilkan 1000 data pertanyaan dan jawaban
all_travel_data = []
all_travel_data.extend(generate_travel_questions_and_answers())

# Membuat DataFrame dari data yang dihasilkan
travel_df = pd.DataFrame(all_travel_data, columns=["Pertanyaan", "Intent", "Jawaban"])

# Menyimpan data ke dalam file CSV
csv_file_path = "travel_questions_and_answers_indonesia.csv"
travel_df.to_csv(csv_file_path, index=False)

csv_file_path