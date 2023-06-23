import streamlit.components.v1 as components
import os

import logging


_RELEASE = True


if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "st_ant_carousel",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3000",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("st_ant_carousel", path=build_dir)

def st_ant_carousel(content:list, carousel_style:dict = None, autoplay:bool = False, autoplaySpeed:int = 3000, dotPosition:str = "bottom", dots:bool = True,  waitForAnimate:bool = True, easing:str = "linear", effect:str = "scrollx",
                    pauseOnDotsHover: bool = False, pauseOnHover:bool = True, animationSpeed:int = 500, vertical:bool=False, adaptiveHeight:bool = False, height:int = 200,key:str = "first_carousel", return_value = False) -> int:
    """

    Parameters
    ----------
    content: list, example: [{"style": {"font-color":"red", "font-size": "20px"}, "content": "<b>1. Entry<b>"},{"style": {"font-color":"blue", "font-size": "20px"}, "content": "<b><h1>2. Entry<b></h1>"}]

    carousel_style: dict, default None - The style of the carousel e.g. {"background-color": "black"}
    autoplay: bool, default False - Whether to scroll automatically
    autoplaySpeed: int, default 3000 - Automatic scrolling interval, in milliseconds
    dotPosition: str, default "bottom" - The position of the dots, which can be one of "top" "bottom" "left" "right" (left and right only work when vertical is true)
    dots: bool, default True - Whether to show the dots
    waitForAnimate: bool, default True - Whether to wait for the animation when switching
    easing: str, default "linear" - Transition interpolation function name
    effect: str, default "scrollx" - Transition effect name "scrollx" "fade"

    pauseOnDotsHover: bool, default False - Whether to pause when hovering over the dots
    pauseOnHover: bool, default True - Whether to pause when hovering over the carousel
    animationSpeed: int, default 500 - Transition animation duration, in milliseconds
    vertical: bool, default False - Whether to scroll vertically
    adaptiveHeight: bool, default False - Whether to adapt to the height of the current slide

    key: str, default "first_carousel" - The key used to save the state of the widget

    return_value: bool, default False - Whether to return the value of the widget - When True the widget will return the selected option, however this will leed to streamlit reloading the page. 
    
    Returns
    -------
    The selected options as a list of strings. (only if return_value is True)

    """
    #  dropdownStyle={{ maxHeight: max_height, overflow: 'auto', width: width_dropdown }}

    #        style={{ width: width_dropdown, marginTop: "10px" }}

    if dotPosition not in ["top", "bottom", "left", "right"]:
        raise ValueError("dotPosition must be one of 'top', 'bottom', 'left', 'right'")
    elif dotPosition in ["left", "right"] and not vertical:
        logging.warning("dotPosition must be one of 'top', 'bottom' when vertical is False")
    elif dotPosition in ["top", "bottom"] and vertical:
        logging.warning("dotPosition must be one of 'left', 'right' when vertical is True")

    #default styling:
    if carousel_style is None:
        carousel_style = {
    "background-color": "#f0f2f5",
    "border-radius": "8px",
    "box-shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
    "padding": "20px",
  
    "width": "100%",
    "customCss": """
        .ant-carousel .slick-dots li button {
            background-color: #a8a9ab !important;
        }
        .ant-carousel .slick-dots li.slick-active button {
            background-color: #78797a !important;
        }
    """
}
    #if slick dots are not style in carousl_style add them
    elif "customCss" not in carousel_style.keys():
        carousel_style["customCss"] = """
        .ant-carousel .slick-dots li button {
            background-color: #a8a9ab !important;
        }
        .ant-carousel .slick-dots li.slick-active button {
            background-color: #78797a !important;
        }
        """
    elif ".slick-dots li button" not in carousel_style["customCss"]:
    
        carousel_style["customCss"] += """
    .ant-carousel .slick-dots li button {
        background-color: #a8a9ab !important;
    }
    .ant-carousel .slick-dots li.slick-active button {
        background-color: #78797a !important;
    }
    """
 
    for content_item in content:
        if "style" not in content_item.keys():
            #add styling
            content_item["style"] = {
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "center",
            "fontFamily": "Arial, sans-serif",
            "background-color": "#c6c6c6",
            "padding": "30px",

        }
            
       
    component_value = _component_func(content=content,key = key, autoplay=autoplay, dotPosition=dotPosition, dots=dots,  waitForAnimate=waitForAnimate, easing=easing, effect=effect,autoplaySpeed=autoplaySpeed,
                                      pauseOnDotsHover=pauseOnDotsHover, pauseOnHover=pauseOnHover, animationSpeed=animationSpeed, vertical=vertical, adaptiveHeight=adaptiveHeight,height=height,carousel_style=carousel_style,
                                      returnValue = return_value
                                      )

    if return_value:
        return component_value
