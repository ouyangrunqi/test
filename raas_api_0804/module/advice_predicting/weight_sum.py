x={
    "status": "SUCCESS",
    "data": {
        "orders": [
            {
                "iuid": "1208005434",
                "prdCode": "LU1128926307",
                "weight": 0.0310,
                "orderType": 1,
                "amount": 310.00,
                "sellUnit": 1,
                "prdName": "JPM Income A (mth) HKD",
                "isin": "LU1128926307",
                "fundType": 2,
                "currentHoldingValue": 1,
                "currentHoldingWeight": 1,
                "targetHoldingValue": 1,
                "targetHoldingWeight": 1
            },
            {
                "iuid": "1208006785",
                "prdCode": "HK0000252160",
                "weight": 0.0612,
                "orderType": 1,
                "amount": 612.47,
                "sellUnit": 1,
                "prdName": "E Fund (HK) China Equity Div A HKD Inc",
                "isin": "HK0000252160",
                "fundType": 1,
                "currentHoldingValue": 1,
                "currentHoldingWeight": 1,
                "targetHoldingValue": 1,
                "targetHoldingWeight": 1
            },
            {
                "iuid": "1208004820",
                "prdCode": "HK0000186863",
                "weight": 0.0639,
                "orderType": 1,
                "amount": 639.63,
                "sellUnit": 1,
                "prdName": "Harvest China A Research Select A HKD",
                "isin": "HK0000186863",
                "fundType": 1,
                "currentHoldingValue": 1,
                "currentHoldingWeight": 1,
                "targetHoldingValue": 1,
                "targetHoldingWeight": 1
            },
            {
                "iuid": "1208006861",
                "prdCode": "LU1467538507",
                "weight": 0.0721,
                "orderType": 1,
                "amount": 721.69,
                "sellUnit": 1,
                "prdName": "AB Asia Income Opps A2 HKD Acc",
                "isin": "LU1467538507",
                "fundType": 2,
                "currentHoldingValue": 1,
                "currentHoldingWeight": 1,
                "targetHoldingValue": 1,
                "targetHoldingWeight": 1
            },
            {
                "iuid": "1208007701",
                "prdCode": "LU1894109211",
                "weight": 0.1166,
                "orderType": 1,
                "amount": 1166.70,
                "sellUnit": 1,
                "prdName": "JPM US Technology A (acc) HKD",
                "isin": "LU1894109211",
                "fundType": 1,
                "currentHoldingValue": 1,
                "currentHoldingWeight": 1,
                "targetHoldingValue": 1,
                "targetHoldingWeight": 1
            },
            {
                "iuid": "1208012653",
                "prdCode": "HK0000359288",
                "weight": 0.1475,
                "orderType": 1,
                "amount": 1475.59,
                "sellUnit": 1,
                "prdName": "Allianz Choice Global Fixed Income Ord A",
                "isin": "HK0000359288",
                "fundType": 2,
                "currentHoldingValue": 1,
                "currentHoldingWeight": 1,
                "targetHoldingValue": 1,
                "targetHoldingWeight": 1
            },
            {
                "iuid": "1208003435",
                "prdCode": "LU0823311666",
                "weight": 0.1492,
                "orderType": 1,
                "amount": 1492.72,
                "sellUnit": 1,
                "prdName": "JPM US Aggregate Bond A (mth) HKD",
                "isin": "LU0823311666",
                "fundType": 2,
                "currentHoldingValue": 1,
                "currentHoldingWeight": 1,
                "targetHoldingValue": 1,
                "targetHoldingWeight": 1
            },
            {
                "iuid": "1208005122",
                "prdCode": "LU1037948541",
                "weight": 0.1613,
                "orderType": 1,
                "amount": 1613.87,
                "sellUnit": 1,
                "prdName": "AB SICAV I Low Volatility Eq A HKD Acc",
                "isin": "LU1037948541",
                "fundType": 1,
                "currentHoldingValue": 1,
                "currentHoldingWeight": 1,
                "targetHoldingValue": 1,
                "targetHoldingWeight": 1
            },
            {
                "iuid": "1208002861",
                "prdCode": "LU0708995401",
                "weight": 0.1972,
                "orderType": 1,
                "amount": 1967.33,
                "sellUnit": 1,
                "prdName": "Franklin US Opportunities A(acc)HKD",
                "isin": "LU0708995401",
                "fundType": 1,
                "currentHoldingValue": 1,
                "currentHoldingWeight": 1,
                "targetHoldingValue": 1,
                "targetHoldingWeight": 1
            }
        ]
    },
    "errors": 1
}


x1 = x["data"]
x2 = x1["orders"]
print(x2)
iii = []
for i in x2:
    ii = i['weight']
    print(ii)
    iii.append(ii)
print(iii)
weight = sum(iii)
if weight == 1:
    print("weight和等于1")
else:
    print("weight和不等于1")



# 字典只支持Key的遍历,，对key，value遍历，用items方法。

# for k,v in x2:
#     i = []
#     if k == "weight":
#         i.append(v)
#         print(i)




