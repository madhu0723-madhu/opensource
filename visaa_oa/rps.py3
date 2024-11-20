vignesh_choice, charan_choice = input().strip().split()
if (vignesh_choice == 'R' and charan_choice == 'S') or \
   (vignesh_choice == 'S' and charan_choice == 'P') or \
   (vignesh_choice == 'P' and charan_choice == 'R'):
    print("Vignesh")
elif (charan_choice == 'R' and vignesh_choice == 'S') or \
     (charan_choice == 'S' and vignesh_choice == 'P') or \
     (charan_choice == 'P' and vignesh_choice == 'R'):
    print("Charan")
else:
    print("NULL")
