days = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']
purchaseDate = input()
daysToDeliver = int(input())
deliveryDayIndex = days.index(purchaseDate) + daysToDeliver
if(deliveryDayIndex > 6):
  deliveryDayIndex = deliveryDayIndex - 7
deliveryDay = days[deliveryDayIndex]
if(daysToDeliver == 0):
  print('chega hoje!')
else:
  print(f"sera entregue {deliveryDay}")