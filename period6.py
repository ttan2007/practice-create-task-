res_list = ["In N Out", "Panda Express", "McDonalds", "Subway", "Coldstone", "PHS Cafeteria"]

new_res = input("What restaurant would you lke to add to the list? ")

def rank_res(new_res, res_list):

    for i in range(len(res_list)): 

        rank = input("Do you like A) " + new_res + " more or B) " + res_list[i] + " more? A/B ")

        if rank == "A":
            res_list.insert(i, new_res)
            return res_list

        elif rank == "B":
            continue 
        
    res_list.append(new_res)
    return res_list

print("Your new ranking of restaurants is ", rank_res(new_res, res_list))