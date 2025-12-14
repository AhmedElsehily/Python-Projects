# tries = 3
# password  = "@hmed"
# print("%"* 50)
# print("  Welcome  to  Fun Day ".center(50,"%"))
# print("%"* 50)
# guss = input("Guss the pass to  contuine: ").strip()

# while guss != password :
#     tries -=1
#     print(f"Wrong password {"last" if tries == 1 else tries} chances left")
#     guss = input("Guss the pass to  contuine: ").strip()
#     if tries == 1 :
#         print("Sorry, try again!!")
#         break
# else:
#     print("Correct Password 👌")

#--------------   Dict implementation  with for loop -----------------#

# programmer = {
#     "Back-end":{
#         "laravel":"php",
#         "Django":"python",
#         "Express.js":"node.js"
#     },
#     "Front-end":{
#         "React.js":"java script",
#         "Flutter web":"dart",
#         "Angular":"java script + type script"
#     },
#     "Mobile Developer":{
#         "Flutter":"dart",
#         "Native (Android)":"java",
#         "React native":"java script",
#         "Native (IOS)":"swift"
#     }
# }
# # print(programmer["Back-end"]["Django"])

# for track in programmer:
#     print("=====================")
#     print(f"{track}  ")
#     print("=====================")
#     print(" Framework  : Language  ".center(30,"*"))
#     for language in programmer[track]:
#         print(f"-{language}  ==>  {programmer [track][language].upper()} ")

#----------------------  Anthor syntax of for loop -----------------------#

# webDeveloper =  {
#     "Back-end":{
#         "laravel":"70%",
#         "Django":"80%",
#         "Express.js":"60%"
#     },
#     "Front-end":{
#         "React.js":"70%",
#         "Flutter":"80%",
#         "Angular":"90%"
#     },
# }

# for track , framework in webDeveloper.items():
#     print("=" * 30)
#     print(f"{track} =>  language are: ")
#     print("=" * 30)
#     for frame, language in framework.items():
#         print(f" Framework is: {frame} progracess: {language}")


# [aaahhhmmmmmeeddds]

def cleanName (name):
    if len(name) == 1:
        return name
    elif name[0] == name[1]:
        return cleanName(name[1:])
    return name[0] + cleanName(name[1:])


print(cleanName("aaahhhmmmmmeeddds"))





























