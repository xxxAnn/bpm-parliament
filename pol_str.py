import pdxpy
f = []
for j in range(0, 100):
    i = j / 100
    f.append(pdxpy.utils.PdxUtil.if_statement({"ig_state_pol_strength_share": [
        {"target": "scope:target_ig"},
        f"value > {i}"
    ]}, [{"add": "0.01"}]))

with open("pol_str.pdx", "w") as file:
    file.write(str(pdxpy.PdxObject(f)))