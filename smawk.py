import numpy as np

def SMAWK(js, A, i_even, minima):   #i_evenは偶数行抽出用のパラメーター

    #これ以上REDUCEできなくなったら、その時のjを返す
    if(len(js) == 1):
        minima[0] = js[0]
        return

    ###REDUCE routine###
    S = [js[0]]  #スタックの宣言
    i = 0

    for q in range(len(js)):
        while(S and (A[i, S[-1]] >= A[i, js[q]]) ): #Sが空じゃなく、前>後である限りは削除し続ける
            del S[-1]
            i = i - i_even

        if(len(S) < (A.shape[0]/i_even) ):   #(Sが空である、もしくは前<後) かつ　スタックのサイズが元の行列以下であるなら
            S.append(js[q])
            i = i + i_even

    ###REDUCE routine###
    #rint(S)
    SMAWK(S, A, i_even*2, minima) #偶数行(0~)のみを抽出するので行の初期値は常に0

    ###奇数行の線形探索###
    #print(js, i_even, minima)
    for i in range(i_even//2, A.shape[0], i_even): #飛ばした行の１つめ(i_even//2)から初めて、元行列の最後の行に達するまで、i_evenずつ飛ばして行を線形探索する。
        minima_tmp = f_inf
        for q in range(len(js)):
            if(A[i, js[q]] < minima_tmp): #i行目で、より小さい値を見つけたらminima[i]を更新
                minima_tmp = A[i, js[q]]
                minima[i] = js[q]
    ###奇数行の線形探索###


A = np.array([[10,17,13,28,23,38,49], [24,28,22,34,24,33,40], [45,44,32,37,23,28,32], [36,33,19,21,6,7,10], [73,66,51,53,34,30,31], [77,66,45,43,21,15,8]])
print(A)
import check_monge as cm
print(cm.check_monge_property((A)))

f_inf = float('inf') #最小値リストの初期値
js = [i for i in range(A.shape[1])]
minima = [f_inf]*A.shape[0] #行最小値格納用配列
SMAWK(js, A, 1, minima) #比較用のスタック、元行列、行探索用（1、2、4...）
print(minima)