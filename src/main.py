"""This module is for thread start."""
import state

if __name__ == '__main__':
    state.kivy = True
    print("Kivy Loading for PyBitmessage......")
    print("Testing")
    from bitmessagemain import main
    main()
