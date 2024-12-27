
def konversiAngkaTerbilang(angka):
	try:
		angka = int(angka) # Mengonversi tipe n ke int dan menghilangkan angka 0 di awal teks jika ada (contoh: "123" -> 123, "0123" -> 123).
		angka = str(angka) # Mengembalikan tipe n menjadi str agar dapat diproses.
	except ValueError:
		return "Input tidak valid"
		
	kamus_angka = {
	    "0": "nol",
	    "1": "satu",
	    "2": "dua",
	    "3": "tiga",
	    "4": "empat",
	    "5": "lima",
	    "6": "enam",
	    "7": "tujuh",
	    "8": "delapan",
	    "9": "sembilan",
	}
	list_satuan_3 = [
	    "/", "ribu", "juta", "miliar", "triliun", "kuadriliun", "kuintiliun", "sekstiliun", "septiliun", "oktiliun", "noniliun", "desiliun", "undesiliun", "duodesiliun", "tredesiliun", "kuattodesiliun", "kuindesiliun"
	]
	
	hasil = []
	hasil_string = ""
	
	len_angka = len(angka)
	
	if len_angka == 1:
		hasil_string = kamus_angka[angka]
		return hasil_string

	idx_satuan_3 = 0
	
	kamus_angka["0"] = "/"
	
	for i in range(len_angka):
		idx = len_angka-1-i
		if i%3 == 2:
			if angka[idx] != "1":
				hasil.insert(0, "ratus")
				hasil.insert(0, kamus_angka[angka[idx]])
			else:
				hasil.insert(0, "ratus")
				hasil.insert(0, "se")
		elif i%3 == 1:
			if angka[idx] != "1":
				hasil.insert(0, "puluh")
				hasil.insert(0, kamus_angka[angka[idx]])
			else:
				if hasil[0] != "/":
					temp = hasil[0]
					hasil[0] = "belas"
					if temp == "satu":
						temp = "se"
					hasil.insert(0, temp)
				else:
					hasil.insert(0, "puluh")
					hasil.insert(0, "se")		
		else:
			hasil.insert(0, list_satuan_3[idx_satuan_3])
			hasil.insert(0, kamus_angka[angka[idx]])
			idx_satuan_3 += 1
	
	for i in range(1, len(hasil)):	
		if hasil[i-1] == "/":
			if hasil[i] == "puluh":
				hasil[i] = "/"
			elif hasil[i] == "ratus":
			    hasil[i] = "/"
			elif hasil[i] in list_satuan_3:
				if i > 4:
					if hasil[i-1] == hasil[i-2] == hasil[i-3] == hasil[i-4] == hasil[i-5] == "/":
						hasil[i] = "/"
		 
	for i in range(len(hasil)):
		if hasil[i] != "/":
			if hasil[i] == "se":
				hasil_string = hasil_string + hasil[i]
			else:
				hasil_string = hasil_string + hasil[i] + " "			   			   			
	return hasil_string


n = input("> ")
while n != 'q':
	print(konversiAngkaTerbilang(n))
	n = input("> ")