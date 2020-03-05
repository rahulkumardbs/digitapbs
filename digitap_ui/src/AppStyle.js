
export const contentStyles = {
    white: (opacity = 1) => `rgba(255, 255, 255, ${opacity})`,
    black: (opacity = 1) => `rgba(0, 0, 0, ${opacity})`,
    topBarHeight: 40,
    footerMenuHeight: 50
  };
export const topBarStyle = {
    position: "fixed",
    top: 0,
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    width: "100%",
    height: contentStyles.topBarHeight+20,
    backgroundColor: contentStyles.white(),
    borderBottom: `1px solid #e7cb01`,
    fontWeight: "bold",
    padding: "0px 0px",
    boxSizing: "border-box"
  };
export const appBody={
    backgroundColor: contentStyles.black(0.00),
    minHeight: "100vh",
    position: "relative"
  }
export const appHome = {
    paddingTop: contentStyles.topBarHeight + 40,
    paddingRight: 20,
    paddingBottom: contentStyles.footerMenuHeight + 20,
    paddingLeft: 20,
    borderSolid:10
  };
export const centerContent = {
    paddingTop: contentStyles.topBarHeight + 140,
    paddingRight: 20,
    paddingBottom: contentStyles.footerMenuHeight + 20,
    paddingLeft: 20,
    borderSolid:10,
    alignItems:'center'
  };
export const primaryButton = {
    width:'44%',
    borderColor:'#e7cb01', 
    color:'#000000', 
    //borderRadius:'50px',
    fontWeight:'bold',
    //color:'#ffffff',
    backgroundColor:'#e7cb01',
    marginLeft:'4%'
  } 
export const successButton = {
    width:'100%', 
    borderColor:'#06962d', 
    backgroundColor:'#06962d', 
    //borderRadius:'50px',
    marginLeft:10,
    color:'#ffffff',
    fontWeight:'bold'
}
export const errorButton = {
    width:'44%',
    borderColor:'#de0808',
    //backgroundColor:'#de0808',
    //borderRadius:'50px',
    marginLeft:10,
    color:'#000',
    fontWeight:'bold',
    marginRight:'4%'
}
export const primaryCard = {
    alignItems:'center' , 
    border:'1px solid #faf8f8', 
    textAlign:'center', 
    borderTopColor:'#e7cb01', 
    borderTopWidth:10, 
    backgroundColor:'#faf8f8' 
};
export const errorCard = {
    alignItems:'center' , 
    border:'1px solid #faf8f8', 
    textAlign:'center', 
    borderTopColor:'#de0808', 
    borderTopWidth:10, 
    backgroundColor:'#faf8f8' 
}
export const processCard = {
    alignItems:'center' , 
    textAlign:'center', 
    borderTopWidth:10, 
    fontSize:'12px'
};
export const successCard = {
    alignItems:'center' , 
    border:'1px solid #faf8f8', 
    textAlign:'center', 
    borderTopColor:'#06962d', 
    borderTopWidth:10, 
    backgroundColor:'#faf8f8' 
}
export const primaryCardTitle = {color:'#e7cb01'};
export const errorCardTitle = {color:'#de0808'};
export const successCardTitle = {color:'#de0808'};
export const captchaImageStyle = {allignContent:'center', width:'50%'};
export const homeInfo = {border:'0.5px solid #e7cb01', padding:10, textAlign:'justify'};
export const homeIcon = { paddingRight:'1px', fontSize:'25px'};
export const homeContent = {paddingTop:'20px'};
export const hideContent = {display:'none'};
export const dispContent = {display:'block'};
export const successIcon = {color:'#06962d', paddingRight:'1px', fontSize:'25px'};
export const notFoundCard = {color:'#000', fontSize:'24px'};
//color:'#e7cb01'