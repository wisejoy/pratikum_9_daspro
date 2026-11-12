# Nama File: list_24060126140223.py
# Pembuat: Bintang Fitra Wisesha
# Tanggal: 1 November 2026
# Deskripsi: Menyelesaikan beberapa permasalahan list menggunakan rekursif
# Catatan: Seluruh bagian APLIKASI sengaja dijadikan komentar agar file ini
#          dapat di-import oleh modul lain (misal lol_24060126140223.py)
#          tanpa mencetak apa pun.

# --------------------------------------------------------------

# DEFINISI DAN SPESIFIKASI TYPE
# ==============================
# Konstruktor menambahkan elemen di awal, notasi prefix
# type List: [] atau [e o List]
# Konstruktor menambahkan elemen di akhir, notasi postfix
# type List: [] atau [List o e]

# --------------------------------------------------------------

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# ===============================
# Konso: elemen, List -> List
#   { Konso(e, L) menghasilkan sebuah list dari e dan L dengan e sebagai elemen pertama
# dari L. }
# Konsi: List, elemen -> List
#   { Konsi(L, e) menghasilkan sebuah list dari L dan e dengan e sebagai elemen terakhir
# dari L. }

# REALISASI
# ==============
def Konso(E: int, L: list) -> list:
    return [E] + L
def Konsi(L: list, E: int) -> list:
    return L + [E]

# APLIKASI
# ==============
# print(Konso(7, [2, 4, 6])) # -> [7, 2, 4, 6]
# print(Konsi([6, 7, 8], 9)) # -> [6, 7, 8, 9]

# --------------------------------------------------------------

# DEFINISI DAN SPESIFIKASI SELEKTOR
# ===============================
# FirstElmt: List tidak kosong -> elemen
#   { FirstElmt(L) mengembalikan elemen pertama dari L. }
# LastElmt: List tidak kosong -> elemen
#   { LastElmt(L) mengembalikan elemen terakhir dari L. }
# Head: List tidak kosong -> List
#   { Head(L) mengembalikan list L tanpa elemen terakhir dari L. }
# Tail: List tidak kosong -> List
#   { Tail(L) mengembalikan list L tanpa elemen pertama dari L. }

# REALISASI
# ==============
def FirstElmt(L: list) -> int:
    return L[0]
def LastElmt(L: list) -> int:
    return L[-1]
def Head(L: list) -> list:
    return L[:-1]
def Tail(L: list) -> list:
    return L[1:]

# APLIKASI
# ==============
# print(FirstElmt([83, 202, 79, 44])) # -> 83
# print(LastElmt([83, 202, 79, 44])) # -> 44
# print(Head([83, 202, 79, 44])) # -> [83, 202, 79]
# print(Tail([83, 202, 79, 44])) # -> [202, 79, 44]

# --------------------------------------------------------------

# DEFINISI DAN SPESIFIKASI PREDIKAT
# ===============================
# isEmpty(L): List -> boolean
#   {isEmpty(L) bernilai True jika List merupakan list kosong.}
# IsOneElmt(L): List -> boolean
#   {IsOneElmt(L) bernilai True jika List hanya memiliki tepat satu elemen.}

# REALISASI
# ==============
def isEmpty(L: list) -> bool:
    return L == []
def IsOneElmt(L: list) -> bool:
    if isEmpty(L):
        return False
    else:
        return Tail(L) == []

# APLIKASI
# ==============
# print(isEmpty([])) # -> True
# print(isEmpty([2, 7])) # -> False
# print(IsOneElmt([8])) # -> True
# print(IsOneElmt([2, 3, 5, 7])) # -> False

# --------------------------------------------------------------

# DEFINISI DAN SPESIFIKASI FUNGSI YANG MENGOPERASIKAN LIST
# ===============================
# NbElmt(L): List -> integer
#   {NbElmt(L) menghasilkan banyaknya elemen dalam list L.}

# REALISASI
# ==============
def NbElmt(L: list) -> int:
    if isEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))

# APLIKASI
# ==============
# print(NbElmt([])) # -> 0
# print(NbElmt([2, 7])) # -> 2
# print(NbElmt([83, 202, 79, 44])) # -> 4

# --------------------Tugas Latihan--------------------

# GLOBAL
# ----------------------------------------------------------------------------------------------------
# DEFINISI DAN SPESIFIKASI
# ============================
# pprintEvalTestCase: list of tuple, string -> (tidak ada, hanya mencetak)
#   { pprintEvalTestCase(l, f) mencetak, untuk setiap tuple argumen di l,
# pemanggilan fungsi f beserta hasil evaluasinya. Fungsi f dinyatakan sebagai string. }
# printEvalTestCase: string, list of tuple, string -> (tidak ada, hanya mencetak)
#   { printEvalTestCase(d, l, f) mencetak judul d dan garis pemisah, lalu
# memanggil pprintEvalTestCase(l, f). }

# REALISASI
# ============================
def pprintEvalTestCase(l: list, f: str) -> None:
    if isEmpty(l):
        return
    else:
        T = FirstElmt(l)
        print(f"{f}{str(T).replace(',)', ')')} = {eval(f'{f}{T}')}")
        pprintEvalTestCase(Tail(l), f)

def printEvalTestCase(d: str, l: list, f: str) -> None:
    print(d)
    print("="*40)
    pprintEvalTestCase(l, f)


# ElmtKeN: integer >= 0, List -> elemen
#   { ElmtKeN(N, L) menghasilkan elemen ke-N dari list L (indeks mulai dari 0).
# Jika N negatif atau N di luar jangkauan list, menghasilkan None. }
def ElmtKeN(N: int, L: list) -> int:
    if N < 0 or isEmpty(L):
        return None
    elif N == 0:
        return FirstElmt(L)
    else:
        return ElmtKeN(N - 1, Tail(L))

# IsMember: elemen, List -> boolean
#   {IsMember(X, L) bernilai True apabila X merupakan elemen dari List.}
def IsMember(X: int, L: list) -> bool:
    if isEmpty(L):
        return False
    elif X == FirstElmt(L):
        return True
    else:
        return IsMember(X, Tail(L))

# Copy: List -> List
#   {Copy(L) menghasilkan List yang identik dengan list asal.}
def Copy(L: list) -> list:
    if isEmpty(L):
        return []
    else:
        return Konso(FirstElmt(L), Copy(Tail(L)))

# Inverse: List -> List
#   {Inverse(L) menghasilkan list L yang dibalik, yaitu yang urutan elemennya
# adalah kebalikan dari list awal.}
def Inverse(L: list) -> list:
    if isEmpty(L):
        return []
    else:
        return Konso(LastElmt(L), Inverse(Head(L)))

# Konkat: 2 List -> List
#   {Konkat(L1, L2) menghasilkan List yang merupakan hasil konkatenasi
# list L1 dan L2.}
def Konkat(L1: list, L2: list) -> list:
    if isEmpty(L1):
        return L2
    else:
        return Konso(FirstElmt(L1), Konkat(Tail(L1), L2))

# SumElmt: List of integer -> integer
#   {SumElmt(L) menghasilkan bilangan bulat yang merupakan jumlah nilai dari seluruh elemen L.
# Jumlah list kosong adalah 0.}
def SumElmt(L: list) -> int:
    if isEmpty(L):
        return 0
    else:
        return FirstElmt(L) + SumElmt(Tail(L))

# AvgElmt: List of integer -> real
#   {AvgElmt(L) menghasilkan bilangan riil yang merupakan rata-rata nilai dari seluruh elemen L.
# Untuk list kosong, menghasilkan 0.0 (berdasarkan kesepakatan).}
def AvgElmt(L: list) -> float:
    if isEmpty(L):
        return 0.0
    else:
        return SumElmt(L) / NbElmt(L)

# MaxElmt: List of integer -> integer
#   {MaxElmt(L) mengembalikan elemen dengan nilai maksimum dari list L.
# Untuk list kosong, menghasilkan None (tidak ada elemen maksimum).}
def MaxElmt(L: list) -> int:
    if isEmpty(L):
        return None
    elif IsOneElmt(L):
        return FirstElmt(L)
    elif FirstElmt(L) > LastElmt(L):
        return MaxElmt(Head(L))
    else:
        return MaxElmt(Tail(L))

# MaxNB: List of integer -> <integer, integer >= 1>
#   {MaxNB(L) menghasilkan tipe bentukan yang berisikan bilangan maksimum
# pada list L dan seberapa banyak bilangan itu muncul di dalam list.
# Untuk list kosong, menghasilkan None.}
Result = tuple[int, int]
def MakeResult(M: int, F: int) -> Result:
    return (M, F)
def CountElement(N: int, L: list) -> int:
    if isEmpty(L):
        return 0
    elif FirstElmt(L) == N:
        return 1 + CountElement(N, Tail(L))
    else:
        return CountElement(N, Tail(L))
def MaxNB(L: list) -> Result:
    if isEmpty(L):
        return None
    else:
        return MakeResult(MaxElmt(L), CountElement(MaxElmt(L), L))

# AddList: 2 List of integer -> List
#   {AddList(L1, L2) menghasilkan list baru yang setiap elemennya adalah
# hasil penjumlahan setiap elemen di L1 dan L2 pada posisi yang sama.
# Jika panjang L1 dan L2 berbeda, menghasilkan None.}
def AddList(L1: list, L2: list) -> list:
    if NbElmt(L1) != NbElmt(L2):
        return None
    elif isEmpty(L1):
        return []
    else:
        return Konso(FirstElmt(L1) + FirstElmt(L2), AddList(Tail(L1), Tail(L2)))

# IsPalindrom: List of character -> boolean
#   {IsPalindrom(L) bernilai True jika L merupakan kata palindrom,
# yakni kata yang sama jika dibaca dari kiri atau kanan.
# List kosong dianggap palindrom (True).}
def IsPalindrom(L: list) -> bool:
    return L == Inverse(L)

# APLIKASI
# ============================
# printEvalTestCase(
#     "1) Contoh penggunaan fungsi ElmtKeN: ",
#     [
#         (0, [5, 10, 15, 20]),
#         (2, [5, 10, 15, 20]),
#         (3, [5, 10, 15, 20]),
#         (1, [42]),
#         (-1, [5, 10, 15, 20]),
#         (4, [5, 10, 15, 20]),
#     ],
#     "ElmtKeN")

# printEvalTestCase(
#     "2) Contoh penggunaan fungsi IsMember: ",
#     [
#         (10, [5, 10, 15, 20]),
#         (7, [5, 10, 15, 20]),
#         (42, [42]),
#         (1, [])
#     ],
#     "IsMember")

# printEvalTestCase(
#     "3) Contoh penggunaan fungsi Copy: ",
#     [
#         ([5, 10, 15, 20],),
#         ([42],),
#         ([],)
#     ],
#     "Copy")

# printEvalTestCase(
#     "4) Contoh penggunaan fungsi Inverse: ",
#     [
#         ([5, 10, 15, 20],),
#         ([42],),
#         ([],)
#     ],
#     "Inverse")

# printEvalTestCase(
#     "5) Contoh penggunaan fungsi Konkat: ",
#     [
#         ([5, 10], [15, 20]),
#         ([42], [7, 14, 21]),
#         ([1, 2, 3], [90]),
#         ([], [1, 2, 3]),
#         ([1, 2, 3], [])
#     ],
#     "Konkat")

# printEvalTestCase(
#     "6) Contoh penggunaan fungsi SumElmt: ",
#     [
#         ([1, 2, 3, 4],),
#         ([5, 10, 15, 20],),
#         ([42],),
#         ([],)
#     ],
#     "SumElmt")

# printEvalTestCase(
#     "7) Contoh penggunaan fungsi AvgElmt: ",
#     [
#         ([1, 2, 3, 4],),
#         ([2, 4, 6],),
#         ([5, 10, 15, 20],),
#         ([42],),
#         ([],)
#     ],
#     "AvgElmt")

# printEvalTestCase(
#     "8) Contoh penggunaan fungsi MaxElmt: ",
#     [
#         ([1, 2, 3, 4],),
#         ([5, 10, 15, 20],),
#         ([7, 14, 21, 21, 14, 7],),
#         ([-5, -2, -9],),
#         ([42],),
#         ([],)
#     ],
#     "MaxElmt")

# printEvalTestCase(
#     "9) Contoh penggunaan fungsi MaxNB: ",
#     [
#         ([1, 2, 3, 4, 4, 2, 4],),
#         ([5, 10, 15, 20, 20, 15, 20],),
#         ([7, 14, 21, 21, 14, 7],),
#         ([42],),
#         ([],)
#     ],
#     "MaxNB")

# printEvalTestCase(
#     "10) Contoh penggunaan fungsi AddList: ",
#     [
#         ([1, 2, 3], [4, 5, 6]),
#         ([5, 10, 15], [20, 25, 30]),
#         ([42], [58]),
#         ([], []),
#         ([1, 2], [3, 4, 5])  # Kasus panjang list tidak sama
#     ],
#     "AddList")

# printEvalTestCase(
#     "11) Contoh penggunaan fungsi IsPalindrom: ",
#     [
#         (['m', 'a', 'd', 'a', 'm'],),
#         (['r', 'a', 'c', 'e', 'c', 'a', 'r'],),
#         (['h', 'e', 'l', 'l', 'o'],),
#         (['k', 'a', 't', 'a', 'k'],),
#         (['a'],),
#         ([],)
#     ],
#     "IsPalindrom")
