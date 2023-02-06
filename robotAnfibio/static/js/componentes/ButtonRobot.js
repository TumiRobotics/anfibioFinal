
class ButtonRobot extends React.Component
{
    constructor(props) 
    {
        super(props);
    }

    render()
    {
        return(
            <a style={{textDecoration: 'none'}} href={this.props.referencia}>
                <button className="mainButton"><i className={this.props.icono}></i>{this.props.nombreBoton}</button>
            </a>
        );
    }
}