""" Command Line for utilmy.
Doc::




"""
HELP1 ="""
Commands:

    


"""
import fire, argparse, os, sys

#############################################################################################
from utilmy.utilmy import log, os_system   

#############################################################################################
try :
   import utilmy 
   dir_utilmy =  utilmy.__path__[0].replace("\\","/")  + "/"
except:   
   dir_utilmy = os.path.dirname(os.path.abspath(__file__)).replace("\\","/") 



#############################################################################################
def run_cli_utilmy():
    """ utilmy command line
    Doc::

        utilmy  h        ### all commands



    """
    import argparse 
    p   = argparse.ArgumentParser()
    add = p.add_argument

    add('task',  metavar='task',  type=str,  nargs="?", help='gpu,gpu_usage')
    add('arg2', metavar='arg2', type=str, nargs="?", help='')
    add('arg3', metavar='arg3', type=str, nargs="?", help='')


    add("--dirin",        type=str, default='gpu',     help = "repo_url")
    add("--repo_dir",     type=str, default="./",      help = "repo_dir")
    add("--dirout",       type=str, default="docs/",   help = "doc_dir")
    add("--fileout",      type=str, default="",        help = "out_file")
    add("--dir_exclude",  type=str, default="",        help = "path1,path2")
    add("--verbose",      type=int, default=0,         help = "hdops://github.com/user/repo/tree/a")
  
    args = p.parse_args()
    do = str(args.task)

    if args.verbose > 0 : 
        log(dir_utilmy)

    if do == 'help':
        print(HELP1) ; return

    if do == 'init':
        pass


    #################################################################################################
    if do == 'gpu_usage': 
        ss=  os_system( f"python {dir_utilmy}/deeplearning/util_dl.py   gpu_usage", doprint=True)
        return None

    if do == 'gpu': 
        ss = os_system( f"python {dir_utilmy}/deeplearning/util_dl.py   gpu_available",doprint=True)
        # log(ss[0])
        return None


    ### Print Help    
    # print(HELP1)
    fire.Fire()



###################################################################################################
if __name__ == "__main__":
    run_cli_utilmy()
    # fire.Fire()


