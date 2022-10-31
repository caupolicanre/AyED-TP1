# while d1 and d2:
#     if d1<d2:
#         aux=d1
#         i1+=1
#         if i1<len(f1)-1:
#             d1=f1[i1]
#             final.append(aux)
#             if aux>d1:
#                 aux=d2
#                 i2+=1
#                 while d2>aux:
#                     final.append(aux)
#         else:                
#             while len(f2)>i2:
#                 aux=d2
#                 i2+=1
#                 final.append(aux)
        
#     elif d2<d1:
#         aux=d2
#         i2+=1
#         if i2<len(f2)-1:
#             d2=f2[i2]
#             final.append(aux)
#             if aux>d2:
#                 aux=d1
#                 i1+=1
#                 while d1>aux:
#                     final.append(aux)
#         else:                
#             while len(f1)>i1:
#                 aux=d1
#                 i1+=1
#                 final.append(aux)
#         # else:
#         #     break
# return final