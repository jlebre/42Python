import time, datetime

secs = time.time()
sci = '{:.2e}'.format(secs)
hoje = datetime.datetime.now()
ano = hoje.strftime("%Y")
mês = hoje.strftime("%b")
dia = hoje.strftime("%d")

# epoch -> 01/01/1970
print(f"Seconds since January 1, 1970: {secs:,.4f} or {sci} in scientific notation")
print(f"{mês} {dia} {ano}")