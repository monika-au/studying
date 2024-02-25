def func(a,b,c,d):
    print(a,b,c,d)

di1 = {"a":11, "b": 12}
di2 = {"b":13, "c":14, "d":15}

a,b1,b2,c,d=di1.get("a"), di1.get("b"), di2.get("b"), di2.get("c"),di2.get("d")

func(a,b1,c,d)
func(a,b2,c,d)