def check_monge_property(a):
    m, n = len(a), len(a[0]) #行列のサイズの取得
    c = 0 #カウンタ変数

    #Monge性の確認コード
    #すべての2行2列の部分行列の単調性を確認すればよい
    #小行列はnC2*mC2個できる
    for i in range(m):
        for j in range(n):
            for k in range(1,(m-i)):
                for l in range(1, (n-j)):
                    if a[i][j] + a[i+k][j+l] > a[i][j+l] + a[i+k][j]:
                        c += 1
                        print("No Monge!")
                        break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break


    if c==0:
        print("Yes Monge!")