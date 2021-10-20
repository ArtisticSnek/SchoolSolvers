def ratio(input1, working = True):
    if "split" in input1:
        formatted = input1.split(" split ")
        total = formatted[0]
        total = float(total)
        ratio = formatted[1]
        ratio = ratio.split(":")
        ratio = [float(i) for i in ratio]
        denom = sum(ratio)
        if working == True:
            wrk = "".join([str(i)+" + " for i in ratio])
            wrk = wrk.rstrip("+ ")
            wrk += f"= {denom}\n"
            print(wrk)
        ratioDec = [i/denom for i in ratio]
        output = ""
        for i in ratioDec:
            temp = float(total)*i
            output+=f" {temp} :"
        if working == True:
            wrk = f"{total}/{denom}={total/denom}\n\n"
            for i in ratio:
                wrk += f"{i}*{total/denom} = {i*(total/denom)}\n"
            print(wrk)
        return output.rstrip(":")
    else:
        formattedIn = input1.split()
        r1 = formattedIn[0]
        r2 = formattedIn[1]
        r1 = r1.split(":")
        stdVal = float(r2)/float(r1[0])
        ratio = [str(float(i)*stdVal) for i in r1]
        output = "".join([i+" : " for i in ratio])
        if working == True:
            print(f"{r2}/{r1[0]} = {stdVal}\n")
            wrk = ""
            for i in r1:
                wrk += f"{i}*{stdVal} = {float(i)*stdVal}\n"
            print(wrk)
        return output.rstrip(" : ")
if __name__ == "__main__":
    while 1:
        try:
            print(ratio(input()))
        except Exception:
            pass
## type something like this
## 10 split 5:5
## 4:4 12
