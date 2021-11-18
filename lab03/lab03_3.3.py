prod_spoz={"maslo": "szt", "mleko": "ml", "chleb": "szt", "banany": "kg", "jogurt": "szt", "szynka": "dag",
           "kukurydza": "puszka"}

prod_szt = {value: key for key, value in prod_spoz.items()}
print(prod_szt)