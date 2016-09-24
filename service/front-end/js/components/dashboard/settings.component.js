import React from "react";
import Constants from '../../constants';
import {withRouter} from 'react-router';


class Settings extends React.Component {

    constructor() {
        super()
    }

    render() {
        return (
            <div>
                <h2>Settings window</h2>
            </div>
        )
    }
}

export default withRouter(Settings);
