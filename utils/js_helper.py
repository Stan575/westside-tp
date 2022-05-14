"""
JavaScript functions
"""

is_in_viewport_script = """function isInViewport(el) {
                               var rect = el.getBoundingClientRect();
                               return (
                                   rect.top >= 0 &&
                                   rect.left >= 0 &&
                                   rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                                   rect.right <= (window.innerWidth || document.documentElement.clientWidth)
                               );}
                           return isInViewport(arguments[0]);"""
