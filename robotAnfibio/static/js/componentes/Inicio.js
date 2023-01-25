class Inicio extends React.Component
{
    constructor(props) 
    {
        super(props);
        this.state = {loading:false}
    }

    componentDidMount()
    {
        if(!this.state.loading)
        {
            setTimeout(()=>{
                this.setState((state,props)=>({
                    loading:true,
                }))
            },2000)
        }
    }

    render()
    {

        console.log('Se ha renderizado')
        if (this.state.loading)
        {
            return(
                <div className="appContainerStart">
                    <div className="position-absolute start-0 bottom-0">
                        <div style={{width: "300px", height: "110px"}}>
                            <div id="btnInicio" className="position-absolute top-0 end-0">
                                <ButtonRobot nombreBoton=' Inicio' icono='fas fa-home' />
                            </div>
                        </div>
                    </div>
                </div>
            );
        }
        else
        {
            return(
                <div className="appContainerIngreso">
                    <div className="logoContainer">
                    </div>
                    <div className="spinner-border" role="status" style={{position:'absolute',bottom:'100px',width:'80px', height:'80px',color:"#9EECD9"}}>
                        <span className="sr-only">Loading ...</span>
                    </div>
                </div>
            );
        }
    }
}