if [ $# -eq 0 ]; then
    echo "Please enter the parameter init/enter/quit/del/help"
    return
fi

help () {
    echo "init: create virtual environment"
    echo "enter: enter virtual environment"
    echo "quit: quit virtual environment"
    echo "del (force): delete virtual environment. If the force parameter is added, the virtual environment will be deleted forcibly"
    echo "export (force): export virtual environment. If the force parameter is added, the requirements.txt file will be overwritten"
    echo "import: import virtual environment"
    echo "install: install libraries"
    echo "uninstall : uninstall libraries"
    echo "help: view help"
}

init () {
    # Get the python version number
    python_version=`python3 -V 2>&1 | awk '{print $1$2}'| awk -F. -v OFS="." '{print $1,$2}'`
    echo "python version number: $python_version"

    # Install python3-venv
    sudo apt install $python_version-venv

    # If the .env folder exists, the virtual environment is not created
    if [ -d ".env" ]; then
        echo "The virtual environment already exists. If you need to create a new virtual environment, please execute the source env.sh del command to delete the virtual environment."
        return
    fi
    python3 -m venv .env
    echo "Create virtual environment"
}

enter () {
    if [ ! -d ".env" ]; then
        echo "The virtual environment does not exist. If you need to create a new virtual environment, please execute the source env.sh init command to create the virtual environment."
        return
    fi

    # If in the virtual environment, do not enter the virtual environment
    if [ ! -z "$VIRTUAL_ENV" ]; then
        echo "Currently in the virtual environment."
        return
    fi

    . .env/bin/activate;
    echo "Enter the virtual environment";
}

quit () {
    if [ ! -d ".env" ]; then
        echo "The virtual environment does not exist. If you need to create a new virtual environment, please execute the source env.sh init command to create the virtual environment."
        return
    fi

    # If not in the virtual environment, do not exit the virtual environment
    if [ -z "$VIRTUAL_ENV" ]; then
        echo "Currently not in the virtual environment."
        return
    fi
    
    deactivate
    echo "Quit the virtual environment"
}

export_libraries () {
    if [ ! -d ".env" ]; then
        echo "The virtual environment does not exist. If you need to create a new virtual environment, please execute the source env.sh init command to create the virtual environment."
        return
    fi

    # If not in the virtual environment, do not exit the virtual environment
    if [ -z "$VIRTUAL_ENV" ]; then
        echo "Currently not in the virtual environment."
        return
    fi

    if [ -f "requirements.txt" ]; then
        if [ $# -eq 1 ]; then
            if [ $1 = "force" ]; then
                rm -f requirements.txt
            else
                echo "Please enter the parameter force"
                return
            fi
        else 
            echo "The requirements.txt file already exists. If you need to update the requirements.txt file, remove requirements.txt and then execute the source env.sh export command to update the requirements.txt file."
            return
        fi
    fi

    pip freeze > requirements.txt
    echo "Export virtual environment"
}

import_libraries () {
    if [ ! -d ".env" ]; then
        echo "The virtual environment does not exist. If you need to create a new virtual environment, please execute the source env.sh init command to create the virtual environment."
        return
    fi

    # If not in the virtual environment, do not exit the virtual environment
    if [ -z "$VIRTUAL_ENV" ]; then
        echo "Currently not in the virtual environment."
        return
    fi

    if [ ! -f "requirements.txt" ]; then
        echo "The requirements.txt file does not exist. If you need to import the requirements.txt file, please execute the source env.sh export command to export the requirements.txt file from other virtual environment."
        return
    fi

    pip install -r requirements.txt
    echo "Import virtual environment"
}

install () {
    if [ ! -d ".env" ]; then
        echo "The virtual environment does not exist. If you need to create a new virtual environment, please execute the source env.sh init command to create the virtual environment."
        return
    fi

    # If not in the virtual environment, do not exit the virtual environment
    if [ -z "$VIRTUAL_ENV" ]; then
        echo "Currently not in the virtual environment."
        return
    fi

    if [ $# -eq 0 ]; then
        echo "Please enter the library name"
        return
    fi

    pip install $1
    echo "Install libraries" $1
}

uninstall () {
    if [ ! -d ".env" ]; then
        echo "The virtual environment does not exist. If you need to create a new virtual environment, please execute the source env.sh init command to create the virtual environment."
        return
    fi

    # If not in the virtual environment, do not exit the virtual environment
    if [ -z "$VIRTUAL_ENV" ]; then
        echo "Currently not in the virtual environment."
        return
    fi

    if [ $# -eq 0 ]; then
        echo "Please enter the library name"
        return
    fi

    pip uninstall $1
    echo "Uninstall libraries" $1
}

del () {
    if [ ! -d ".env" ]; then
        echo "The virtual environment does not exist. Failed to delete the virtual environment."
        return
    fi
    if [ ! -z "$VIRTUAL_ENV" ]; then
        if [ $# -eq 1 ]; then
            if [ $1 = "force" ]; then
                quit
            else
                echo "Please enter the parameter force"
                return
            fi
        else 
            echo "Currently in the virtual environment. Failed to delete the virtual environment. if you need to delete the virtual environment, please exit the virtual environment and then execute the source env.sh del command to delete the virtual environment. Or execute the source env.sh del force command to force delete the virtual environment."
            return
        fi
    fi

    rm -rf .env
    echo "Delete virtual environment"
}

if [ $1 = "init" ]; then
    init
elif [ $1 = "enter" ]; then 
    enter
elif [ $1 = "quit" ]; then
    quit
elif [ $1 = "del" ]; then
    if [ $# -eq 1 ]; then
        del
    elif [ $# -eq 2 ]; then
        del $2
    fi
elif [ $1 = "export" ]; then
    if [ $# -eq 1 ]; then
        export_libraries
    elif [ $# -eq 2 ]; then
        export_libraries $2
    else
        help
    fi
elif [ $1 = "import" ]; then
    import_libraries
elif [ $1 = "install" ]; then
    libraries=""
    for arg in $*; do
        if [ $arg = "install" ]; then
            continue
        fi
        libraries="$libraries $arg"
    done
    install "$libraries"
elif [ $1 = "uninstall" ]; then
    libraries=""
    for arg in $*; do
        if [ $arg = "uninstall" ]; then
            continue
        fi
        libraries="$libraries $arg"
    done
    uninstall "$libraries"
else
    help
fi
