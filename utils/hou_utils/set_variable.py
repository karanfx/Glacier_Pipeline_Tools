import hou

# Set a custom environment variable
show_name = "Show01"
shot_name = "Shot_AB01"
user_name = "perman"
shot_dir = show_name + "/" + shot_name + "/" + user_name
variables = { "SHOW": show_name, "SHOT": shot_name,
             "SHOT_DIR":shot_dir,"USER":user_name}


for var_name,var_val in variables.items():
    # Set the environment variable
    hou.hscript("setenv {}={}".format(var_name, var_val))

    # print("Environment variable {} set to: {}".format(var_name, hou.getenv(var_name)))