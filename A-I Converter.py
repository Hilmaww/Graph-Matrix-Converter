def main():
    print("Welcome!")
    con = int(input("Konversi Adjacency-to-Incidence (1) atau Incidence-to-Adjacency (2)?: "))
    while con!=1 and con!=2:
        print("Masukkan tidak valid. Silahkan masukan ulang!")
        con = int(input("Konversi Adjacency-to-Incidence (1) atau Incidence-to-Adjacency (2)?: "))
    if con==1:
        A_to_I()
    elif con==2:
        I_to_A()
        

def print_matriks(matriks):
    for i in range(len(matriks)):
        print("| ", end="")
        for j in range(len(matriks[0])):
            print(matriks[i][j], end=" ")
        print(" |")
    print()

def A_to_I():
    node = int(input("Masukkan jumlah simpul: "))
    A = [[0 for i in range(node)] for j in range(node)]
    R = []
    print("Masukkan matriks Adjacency!")
    for i in range(node):
        for j in range(node):
            print("Baris ke-", i+1, "kolom ke-", j+1, end=": ")
            A[i][j] = int(input())
            if j>=i:
                if A[i][j] == 1:
                    R.append((i, j))

    print_matriks(A)

    I = [[0 for i in range(len(R))] for j in range(len(R))]
    for i in range(len(R)):
        if R[i][0]!=R[i][1]:
            I[R[i][0]][i] +=1
            I[R[i][1]][i] +=1
        elif R[i][0]==R[i][1]:
            I[R[i][0]][i] +=1
    
    print_matriks(I)

def I_to_A():
    v_nom = int(input("Masukkan Banyaknya Vertex (poin): "))
    e_nom = int(input("Masukkan Banyaknya Edge (garis): "))
    
    # Inisiasi Matrix kosong Incidence
    M_matrix = [[ 0 for j in range(e_nom)] for i in range(v_nom)]
    
    # Meminta input
    for i in range(v_nom): #baris
        for j in range(e_nom): #kolom
            M_matrix[i][j] = int(input(f"vertex {i+1} edge {j+1}: "))
        print()
    
    # Inisiasi Matrix Baris
    # Mengubah Matrix Incidence menjadi transpose-nya
    e = [ [M_matrix[j][i] for j in range(v_nom)] for i in range(e_nom)] 

    def check_incident(matrix):
        # Sub-Program mengecek Matrix Incident
        # Input: Matriks Transpose dari Matriks Incident
        # Output: Matrix Adj yang sudah diproses

        # Variabel:
            # adj: matrix adj yang akan dihasilkan
            # check_matrix: matrix tinjauan untuk tiap barisnya
            # any: Variabel penanda bahwa ada node yang berhubungan
            # alone: Variabel penanda bahwa node-nya sndiri..

        # Processing matrix baris e

        # Inisiasi Matrix Adj yang akan dihasilkan
        global adj
        adj = [ [ 0 for j in range(v_nom)] for i in range(v_nom)]
        
        
        def adj_matrix(n, m):
            # Fungsi Membuat Kembaran untuk adj Matrix
            # Input: Koordinat Matrix adj yang ditemukan 
            # Output: Matrix adj yang telah diproses

            adj[n][m], adj[m][n] = 1, 1

        def adj_refleksif(vertex):
            # Fungsi membuat self-pointing node pada adj Matrix
            # Input: Baris. Pada baris berapa alone vertex ini ditemukan
            # Output: Matrix adj yang telah diproses. 
            #          Memberi nilai 1 pada koordinat [(1,1), (2,2), (3,3), (n,n), ..] 
            #          menunjukkan bahwa vertex tersebut punya edge yang mengarah pada dirinya sendiri
            adj[vertex][vertex] = 1

        # Mengecek tiap baris pada M_matrix
        for baris in range(len(matrix)):
            check_matrix = matrix[baris]
            # print(f"Edge ke {baris}: ", end="") # Untuk Debugging
            any = 0         # Variabel penanda bahwa ada node yang berhubungan
            alone = 0       # Variabel penanda bahwa node-nya sndiri..

            for i in range(0, e_nom):
                if  i<len(matrix[baris]):
                    if matrix[baris][i] == 1:
                            alone +=i # Bila ada 1 pada baris tersebut, berpotensi alone
                for j in range(i+1, v_nom):
                    if matrix[baris][i]==matrix[baris][j] and matrix[baris][i] == 1: # Bila ketemu 1 di baris yang sama
                        print()
                        # print(f"Vertex ke {i} dengan Vertex ke {j}") # Untuk Debugging
                        adj_matrix(i, j)
                        any+=1
            if any == 0 and (1 in check_matrix): # Kalau dia sndiri dan ada 1
                # print("Vertex sendiri") #Untuk Debugging
                adj_refleksif(alone)

    check_incident(e)
    
    print("Matrix Incidence")

    for i in range(v_nom): #baris
        for j in range(e_nom): #kolom
            print(M_matrix[i][j], end=" ")
        print()

# kalau mau cek matrix barisnya (M_matrix transpose)
#    print("Matrix Baris")
#    for i in range(e_nom): #baris
#        for j in range(v_nom): #kolom
#            print(e[i][j], end=" ")
#        print()
        
    
    print("Matrix Adj")

    for i in range(v_nom): #baris
        for j in range(v_nom): #kolom
            print(adj[i][j], end=" ")
        print()

main()