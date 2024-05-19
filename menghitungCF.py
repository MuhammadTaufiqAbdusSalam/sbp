# Definisikan kode menu, kategori, dan aturan sebagai array atau dictionary
penyakit_codes = ["J001", "J002", "J004", "J005"]
gejala_codes = ["G01", "G02", "G03", "G04", "G05", "G06", "G07", "G08", "G09", "G10", "G11", "G12", "G13", "G14", "G15", "G16", "G17", "G18", "G19"]

# Definisikan kode menu, kategori, dan aturan sebagai dictionary
rules = {
    "J001": ["G02", "G03", "G04", "G05", "G06", "G08", "G13"],
    "J002": ["G01", "G02", "G03", "G05", "G06", "G07", "G08", "G10", "G12", "G13", "G15", "G16", "G17", "G19"],
    "J004": ["G01", "G02", "G03", "G05", "G07", "G08", "G09", "G10", "G11", "G12", "G13", "G14"],
    "J005": ["G02", "G05", "G06", "G07", "G08", "G10", "G13", "G16", "G17"]
}

# Definisi Term CF
term_cf = {
    "Tidak": 0,
    "Terkadang": 0.5,
    "Ya": 1
}

# Definisikan kategori dan nilai MB-nya sebagai dictionary
user_input = {
    "G01": ["tidak berminyak", "Terkadang", 0.5],
    "G02": ["segar dan halus", "Terkadang", 0.5],
    "G03": ["bahan-bahan kosmetik mudah menempel di kulit", "Tidak", 0],
    "G04": ["terlihat sehat", "Tidak", 0],
    "G05": ["tidak berjerawat", "Tidak", 0],
    "G06": ["mudah mengalami masalah kosmetik", "Terkadang", 0.5],
    "G07": ["pori-pori kulit besar  terutama di area hidung, dagu dan pipi", "Terkadang", 0.5],
    "G08": ["kulit wajah terlihat mengkilat", "Terkadang", 0.5],
    "G09": ["kulit terlihat kering sekali", "tidak", 0],
    "G10": ["pori-pori halus", "Terkadang", 0.5],
    "G11": ["tekstur kulit wajah tipis", "Terkadang", 0.5],
    "G12": ["cepat menampakkan kerutan kerutan", "Terkadang", 0.5],
    "G13": ["sebagian wajah terlihat berminyak", "Terkadang", 0.5],
    "G14": ["sebagian wajah terlihat kering", "Terkadang", 0.5],
    "G15": ["susah mendapatkan polesan kosmetik yang sempurna", "Tidak", 0],
    "G16": ["mudah alergi", "Terkadang", 0.5],
    "G17": ["mudah iritasi dan terluka", "Terkadang", 0.5],
    "G18": ["kulit mudah terlihat kemerahan", "Ya", 1],
    "G19": ["gatal jika terkena sinar matahari", "Tidak", 0]
}

# Input pakar berupa dictionary dengan kode menu sebagai kunci dan kategori serta nilai MD sebagai nilai
pakar_input = {
    "J001": [("G02", "segar dan halus", 1.0), ("G03", "bahan-bahan kosmetik mudah menempel di kulit", 1.0), ("G04", "terlihat sehat", 0.5), ("G05", "tidak berjerawat", 0.5),("G06", "mudah mengalami masalah kosmetik", 0.5), ("G08", "kulit wajah terlihat mengkilat", 0.5), ("G13", "sebagian wajah terlihat berminyak", 0.5)],
    "J002": [("G01", "tidak berminyak", 0.5), ("G02", "segar dan halus", 0.5), ("G03", "bahan-bahan kosmetik mudah menempel di kulit", 0.5), ("G05", "tidak berjerawat", 1.0), ("G06", "mudah mengalami masalah kosmetik", 0.5), ("G07", "pori-pori kulit besar  terutama di area hidung, dagu dan pipi", 1.0), ("G08", "Usia Tuakulit wajah terlihat mengkilat", 0.5), ("G10", "pori-pori halus", 0.5), ("G12", "cepat menampakkan kerutan kerutan", 1.0), ("G13", "sebagian wajah terlihat berminyak", 1.0), ("G15", "susah mendapatkan polesan kosmetik yang sempurna", 0.5), ("G16", "mudah alergi", 0.5), ("G17", "mudah iritasi dan terluka", 0.5), ("G19", "gatal jika terkena sinar matahari", 0.5)],
    "J004": [("G01", "tidak berminyak", 1.0), ("G02", "segar dan halus", 0.5), ("G03", "bahan-bahan kosmetik mudah menempel di kulit", 0.5), ("G05", "tidak berjerawat", 0.5), ("G07", "pori-pori kulit besar  terutama di area hidung, dagu dan pipi", 1.0), ("G08", "kulit wajah terlihat mengkilat", 0.5), ("G09", "kulit terlihat kering sekali", 0.5), ("G10", "pori-pori halus", 0.5), ("G11", "tekstur kulit wajah tipis", 1.0), ("G12", "cepat menampakkan kerutan kerutan", 0.5), ("G13", "sebagian wajah terlihat berminyak", 0.5), ("G14", "sebagian wajah terlihat kering", 0.5)],
    "J005": [("G02", "segar dan halus", 0.5), ("G05", "tidak berjerawat", 0.5), ("G06", "mudah mengalami masalah kosmetik", 1.0), ("G07", "pori-pori kulit besar  terutama di area hidung, dagu dan pipi", 1.0), ("G08", "kulit wajah terlihat mengkilat", 0.5), ("G10", "pori-pori halus", 0.5), ("G13", "sebagian wajah terlihat berminyak", 0.5), ("G16", "mudah alergi", 1.0), ("G17", "mudah iritasi dan terluka", 1.0)]
}

# Input pakar berupa dictionary dengan kode menu sebagai kunci dan kategori serta nilai MD sebagai nilai
hitung_cf = {
    "J001": [("G02", "segar dan halus", 0.5, 1.0), ("G03", "bahan-bahan kosmetik mudah menempel di kulit", 0, 1.0), ("G04", "terlihat sehat", 0,  0.5), ("G05", "tidak berjerawat", 0, 0.5),("G06", "mudah mengalami masalah kosmetik", 0.5, 0.5), ("G08", "kulit wajah terlihat mengkilat", 0.5, 0.5), ("G13", "sebagian wajah terlihat berminyak", 0.5, 0.5)],
    "J002": [("G01", "tidak berminyak", 0.5, 0.5), ("G02", "segar dan halus", 0.5, 0.5), ("G03", "bahan-bahan kosmetik mudah menempel di kulit", 0, 0.5), ("G05", "tidak berjerawat", 0, 1.0), ("G06", "mudah mengalami masalah kosmetik", 0.5, 0.5), ("G07", "pori-pori kulit besar  terutama di area hidung, dagu dan pipi", 0.5, 1.0), ("G08", "Usia Tuakulit wajah terlihat mengkilat", 0.5, 0.5), ("G10", "pori-pori halus", 0.5, 0.5), ("G12", "cepat menampakkan kerutan kerutan", 0.5, 1.0), ("G13", "sebagian wajah terlihat berminyak", 0.5, 1.0), ("G15", "susah mendapatkan polesan kosmetik yang sempurna", 0, 0.5), ("G16", "mudah alergi", 0.5, 0.5), ("G17", "mudah iritasi dan terluka", 0.5, 0.5), ("G19", "gatal jika terkena sinar matahari", 0, 0.5)],
    "J004": [("G01", "tidak berminyak", 0.5, 1.0), ("G02", "segar dan halus", 0.5, 0.5), ("G03", "bahan-bahan kosmetik mudah menempel di kulit", 0, 0.5), ("G05", "tidak berjerawat", 0, 0.5), ("G07", "pori-pori kulit besar  terutama di area hidung, dagu dan pipi", 0.5, 1.0), ("G08", "kulit wajah terlihat mengkilat", 0.5, 0.5), ("G09", "kulit terlihat kering sekali", 0, 0.5), ("G10", "pori-pori halus", 0.5, 0.5), ("G11", "tekstur kulit wajah tipis", 0.5, 1.0), ("G12", "cepat menampakkan kerutan kerutan", 0.5, 0.5), ("G13", "sebagian wajah terlihat berminyak", 0.5, 0.5), ("G14", "sebagian wajah terlihat kering", 0.5, 0.5)],
    "J005": [("G02", "segar dan halus", 0.5, 0.5), ("G05", "tidak berjerawat", 0, 0.5), ("G06", "mudah mengalami masalah kosmetik", 0.5, 1.0), ("G07", "pori-pori kulit besar  terutama di area hidung, dagu dan pipi", 0.5, 1.0), ("G08", "kulit wajah terlihat mengkilat", 0.5, 0.5), ("G10", "pori-pori halus", 0.5, 0.5), ("G13", "sebagian wajah terlihat berminyak", 0.5, 0.5), ("G16", "mudah alergi", 0.5, 1.0), ("G17", "mudah iritasi dan terluka", 0.5, 1.0)]
}

def calculate_combination_cf(penyakit):
    cf_combination = 1
    for gejala in user_input.keys():
        for data in hitung_cf[penyakit]:
            if gejala == data[0]:
                cf_combination *= data[2] * data[3]
                break
    return cf_combination

def calculate_aggregated_cf(penyakit):
    cf_combinations = []
    for gejala in user_input.keys():
        for data in hitung_cf[penyakit]:
            if gejala == data[0]:
                cf_combinations.append(data[2] * data[3])
                break

    cf_aggregated = cf_combinations[0]
    for cf in cf_combinations[1:]:
        cf_aggregated = cf_aggregated + cf - (cf_aggregated * cf)

    return cf_aggregated

def calculate_percentage(cf_combination, cf_aggregated):
    return cf_aggregated * 100

def calculate_cf(penyakit):
    cf_combination = calculate_combination_cf(penyakit)
    cf_aggregated = calculate_aggregated_cf(penyakit)
    percentage = calculate_percentage(cf_combination, cf_aggregated)
    
    return percentage

print("\nCertainty Factor Gabungan:")
print("Kode Penyakit   |       CF Gabungan")
print("-----------------------------------")
for penyakit in rules.keys():
    i = penyakit_codes.index(penyakit)
    cf_percentage = calculate_cf(penyakit)
    print(f"{penyakit}\t\t|\t{cf_percentage:.2f}%")
