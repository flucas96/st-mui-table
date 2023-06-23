import React, { useEffect} from "react";
import {
  ComponentProps,
  Streamlit,
  withStreamlitConnection,

} from "streamlit-component-lib";
import { Carousel } from 'antd';


const CarouselComponent = (props: ComponentProps) => {

  const {content, autoplay, autoplaySpeed,dotPosition, dots, waitForAnimate,easing,effect, key,pauseOnDotsHover, pauseOnHover, animationSpeed, vertical, adaptiveHeight,height,carousel_style,returnValue} = props.args; //Python Args


  useEffect(() => {
    Streamlit.setFrameHeight(height);
  }, []);

  const contentWithCamelCase = content.map((slide: any) => {
    const styleWithCamelCase = Object.entries(slide.style).reduce(
      (acc, [k, v]) => {
        const modifiedKey = k.replace(/-(.)/g, (match, char) =>
          char.toUpperCase()
        );
        return { ...acc, [modifiedKey]: v };
      },
      {}
    );
    return { ...slide, style: styleWithCamelCase };
  });


  const onChange = (currentSlide: number) => {
    if (returnValue) {
      Streamlit.setComponentValue(currentSlide);
    }
  };
 
  // Convert carousel_style to camelCase
  const carouselStyleWithCamelCase = Object.entries(carousel_style).reduce(
    (acc, [k, v]) => {
      const modifiedKey = k.replace(/-(.)/g, (match, char) =>
        char.toUpperCase()
      );
      return { ...acc, [modifiedKey]: v };
    },
    {}
  );
    return (
      <>
       <style dangerouslySetInnerHTML={{__html: carousel_style.customCss}}></style>

      <Carousel
        afterChange={returnValue ? (currentSlide: number) => { Streamlit.setComponentValue(currentSlide) } : undefined}
        autoplay={autoplay}
        autoplaySpeed={autoplaySpeed}
        dotPosition={dotPosition}
        dots={dots}
        waitForAnimate={waitForAnimate}
        easing={easing}
        effect={effect}
        key={key}
        pauseOnDotsHover={pauseOnDotsHover}
        pauseOnHover={pauseOnHover}
        speed={animationSpeed}
        vertical={vertical}
        adaptiveHeight={adaptiveHeight}
        style={carouselStyleWithCamelCase} // Apply the transformed carousel_style

      >
 {contentWithCamelCase.map((slide: any, index: number) => (
        <div key={index}>
          <div
            style={slide.style}
            dangerouslySetInnerHTML={{ __html: slide.content }}
          ></div>
        </div>
      ))}
      </Carousel>
      </>
    );

  };
  
  export default withStreamlitConnection(CarouselComponent);