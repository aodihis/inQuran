UPDATE your_table_name
SET id_title = CASE 
    WHEN en_title = 'Allah has no son' THEN 'Allah tidak punya anak'
    WHEN en_title = 'Allah is near (qareeb)' THEN 'Allah itu dekat (qareeb)'
    WHEN en_title = 'Allah knows the unseen' THEN 'Allah mengetahui yang gaib'
    WHEN en_title = 'About the grave' THEN 'Tentang kuburan'
    WHEN en_title = 'Lowering Gaze' THEN 'Menundukkan pandangan'
    WHEN en_title = 'Haram & Forbidden' THEN 'Haram & Terlarang'
    WHEN en_title = 'On Alcohol' THEN 'Tentang Alkohol'
    WHEN en_title = 'Allah\'s Mercy' THEN 'Rahmat Allah'
    WHEN en_title = 'Allah\'s Protection' THEN 'Perlindungan Allah'
    WHEN en_title = 'On Animals' THEN 'Tentang Hewan'
    WHEN en_title = 'About Arrogance' THEN 'Tentang Kesombongan'
    WHEN en_title = 'Compulsion into Religion' THEN 'Pemaksaan ke dalam Agama'
    WHEN en_title = 'On Deception' THEN 'Tentang Penipuan'
    WHEN en_title = 'About Difficulties' THEN 'Tentang Kesulitan'
    WHEN en_title = 'About Disbelievers' THEN 'Tentang Orang Kafir'
    WHEN en_title = 'Doing Good to Others' THEN 'Berbuat Baik kepada Orang Lain'
    WHEN en_title = 'Family Ties / Kinship' THEN 'Ikatan Keluarga / Kerabat'
    WHEN en_title = 'Halal / Permissible' THEN 'Halal / Diperbolehkan'
    WHEN en_title = 'On Happiness' THEN 'Tentang Kebahagiaan'
    WHEN en_title = 'Hardship' THEN 'Kesulitan'
    WHEN en_title = 'Health' THEN 'Kesehatan'
    WHEN en_title = 'Helping Others' THEN 'Menolong Orang Lain'
    WHEN en_title = 'Hijab' THEN 'Hijab'
    WHEN en_title = 'Homosexuality' THEN 'Homoseksualitas'
    WHEN en_title = 'Hope' THEN 'Harapan'
    WHEN en_title = 'Human Body' THEN 'Tubuh Manusia'
    WHEN en_title = 'Jannah' THEN 'Surga'
    WHEN en_title = 'Prophet Jesus (as)' THEN 'Nabi Isa (as)'
    WHEN en_title = 'On Justice' THEN 'Tentang Keadilan'
    WHEN en_title = 'Verses on Killing' THEN 'Ayat tentang Membunuh'
    WHEN en_title = 'Kindness to others' THEN 'Kebaikan kepada orang lain'
    WHEN en_title = 'On Knowledge' THEN 'Tentang Pengetahuan'
    WHEN en_title = 'Listening to Qur\'an' THEN 'Mendengarkan Al-Qur\'an'
    WHEN en_title = 'Allah Loves' THEN 'Allah Mencintai'
    WHEN en_title = 'Qur\'an on Love' THEN 'Al-Qur\'an tentang Cinta'
    WHEN en_title = 'On Lying' THEN 'Tentang Berbohong'
    WHEN en_title = 'Marriage' THEN 'Pernikahan'
    WHEN en_title = 'Mothers' THEN 'Ibu'
    WHEN en_title = 'Beauty of Nature' THEN 'Keindahan Alam'
    WHEN en_title = 'Not Giving Up' THEN 'Tidak Menyerah'
    WHEN en_title = 'Obedience To Parents' THEN 'Ketaatan Kepada Orang Tua'
    WHEN en_title = 'Patience' THEN 'Kesabaran'
    WHEN en_title = 'Peace' THEN 'Perdamaian'
    WHEN en_title = 'People of the Book' THEN 'Ahli Kitab'
    WHEN en_title = 'On The Prayer' THEN 'Tentang Sholat'
    WHEN en_title = 'Pregnancy' THEN 'Kehamilan'
    WHEN en_title = 'Prophet Hud (as)' THEN 'Nabi Hud (as)'
    WHEN en_title = 'About Prostitution' THEN 'Tentang Prostitusi'
    WHEN en_title = 'Respecting Other Religions' THEN 'Menghormati Agama Lain'
    WHEN en_title = 'Respecting Others' THEN 'Menghormati Orang Lain'
    WHEN en_title = 'Overcoming Sadness' THEN 'Mengatasi Kesedihan'
    WHEN en_title = 'About Shirk' THEN 'Tentang Syirik'
    WHEN en_title = 'On Sin' THEN 'Tentang Dosa'
    WHEN en_title = 'Slander' THEN 'Fitnah'
    WHEN en_title = 'Stealing' THEN 'Mencuri'
    WHEN en_title = 'Strength' THEN 'Kekuatan'
    WHEN en_title = 'Tyranny' THEN 'Kezaliman'
    WHEN en_title = 'On The Universe' THEN 'Tentang Alam Semesta'
    WHEN en_title = 'Vanity' THEN 'Kesombongan'
    WHEN en_title = 'War' THEN 'Perang'
    WHEN en_title = 'Wife' THEN 'Istri'
    WHEN en_title = 'On Women' THEN 'Tentang Wanita'
    WHEN en_title = 'On Youth' THEN 'Tentang Pemuda'
    WHEN en_title = 'Allah\'s wrath' THEN 'Kemarahan Allah'
    ELSE id_title
END;
