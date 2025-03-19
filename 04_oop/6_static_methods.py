class Demo_Static_Method:
    @staticmethod
    def tell_me_about_class():
        print("This class is testing static methods.")

an_object = Demo_Static_Method()

Demo_Static_Method.tell_me_about_class()
an_object.tell_me_about_class() # python internally redirects this code to the above one, this way is not recommended.