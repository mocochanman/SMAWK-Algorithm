# SMAWK-Algorithm

##samwk.py
###凹Monge propertyを持つ行列$A$に対して、_SMAWK Algorithm_を用いて高速な行最小値探索を行います。

###入力：numpy.array(Matrix A)
###出力：各行_i_における最小値の位置_(i, j)_

##check_monge.py
###行列_A_が凹Monge propertyを持つかどうかを判定します。

###入力：numpy.array(Matrix A)
###出力：Yes or No

###四角不等式の不等号を逆にすることで、凸Monge propertyの判定も行うことが可能です。
