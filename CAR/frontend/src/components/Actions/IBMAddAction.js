import React, { useState } from "react";
import axios from "axios";

import Image from "react-bootstrap/Image";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";
import { Trash } from "react-bootstrap-icons";

import SetQuantity from "../SetActionInputs/SetQuantity";
import SetDropwise from "../SetActionInputs/SetDropwise";
import SetAtmosphere from "../SetActionInputs/SetAtmosphere";

import JSMEModal from "../MolDrawer/JSMEModal";
import MolAlert from "../MolDrawer/MolAlert";

const IBMAddAction = ({ action, actionno, updateAction, handleDelete }) => {
  const [Action, setAction] = useState(action);
  const [Show, setShow] = useState(false);
  const [ShowAlert, setShowAlert] = useState(false);

  const actiontype = Action.actiontype;
  const id = Action.id;
  const Smiles = Action.materialsmiles;
  const SVG = Action.materialimage;

  function handleShow() {
    setShow(true);
  }

  function handleClose(smiles) {
    setShow(false);
    var mol = window.checkmol(smiles);
    if (mol) {
      setShowAlert(false);
      var origmol = window.checkmol(Smiles);
      var origsmiles = origmol.get_smiles();
      var canonsmiles = mol.get_smiles();
    } else {
      setShowAlert(true);
      console.log("mol invalid");
    }
    if (canonsmiles !== origsmiles) {
      patchSVG(canonsmiles);
    }
  }

  async function patchSVG(value) {
    try {
      const patchresponse = await axios.patch(
        `api/IBM${Action.actiontype}actions/${id}/`,
        {
          materialsmiles: value,
        }
      );
      const fetchresponse = await axios.get(
        `api/IBM${Action.actiontype}actions/${id}/`
      );
      setAction(fetchresponse.data);
    } catch (error) {
      console.log(error);
    }
    console.log(value);
  }

  return (
    <Container key={actionno}>
      <h5>
        {actionno}. {actiontype.capitalize()}
      </h5>
      <Row>
        <Col>
          <MolAlert show={ShowAlert}></MolAlert>
          <JSMEModal
            show={Show}
            handleClose={handleClose}
            smiles={Smiles}
          ></JSMEModal>
          <Button className="editcompound" onClick={() => handleShow()}>
            <Image src={SVG} alt={action.material} fluid />
          </Button>
          <SetQuantity
            action={Action}
            updateAction={updateAction}
            name={"material"}
          ></SetQuantity>
          <SetDropwise
            action={Action}
            updateAction={updateAction}
          ></SetDropwise>
          <SetAtmosphere
            action={Action}
            updateAction={updateAction}
          ></SetAtmosphere>
        </Col>
      </Row>
      <Row>
        <Col>
          <Button key={id} onClick={() => handleDelete(actiontype, id)}>
            <Trash></Trash>
          </Button>
        </Col>
      </Row>
    </Container>
  );
};

export default IBMAddAction;
