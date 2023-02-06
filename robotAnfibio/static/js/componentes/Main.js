class Main extends React.Component
{
    constructor(props) 
    {
        super(props);
    }

    render()
    {
        return(
            <div className="appContainerMain">
                <div className="textoMain">

                </div>
                {/*<p className="textoApp">TUMI ANFIBIO 2022 - Limpieza de barcos</p>*/}
                <div className="position-absolute start-0 bottom-0">
                    <div style={{width: "300px", height: "110px"}}>
                        <div id="btnInicio" className="position-absolute top-0 end-0">
                            <ButtonRobot nombreBoton={this.props.nombreBoton} icono={this.props.icono} />
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}