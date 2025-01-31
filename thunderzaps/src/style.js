const style = {
    main: {
        width: "100vw",
        height: "100vh",
        margin: 0,
        
        display: "flex",
        flexDirection: "row",
    },
    
    sidebar: {
        width: "20vw",
        height: "100vh",
        margin: 0,
        backgroundColor: "#60a060",
        
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        paddingTop: "1em",
        paddingBottom: "1em",
        gap: "50px",
    },
    
    content: {
        width: "80vw",
        height: "100vh",
    },
    
    tabButton: {
        width: "100%",
        border: "none",
        backgroundColor: "#b0f0b0",
        padding: "20px",
    },
    
    selectButton: {
        width:"100%",
        border: "none",
        backgroundColor: "#c5d9b4",
        padding: "20px",
    }
};

export default style;