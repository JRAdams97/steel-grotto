using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour {
    
    private Camera mainCamera;

    void Start() {
        mainCamera = GetComponent<Camera>();
    }

    void Update() {
        if (mainCamera != null) {
            if (Input.GetKeyDown(KeyCode.W)) {
                mainCamera.transform.position += mainCamera.transform.forward * 4f;
            }

            if (Input.GetKeyDown(KeyCode.S)) {
                mainCamera.transform.position -= mainCamera.transform.forward * 4f;
            }

            if (Input.GetKeyDown(KeyCode.A)) {
                Vector3 rotateVal = new Vector3(0, -90, 0);
                mainCamera.transform.Rotate(rotateVal);
            }

            if (Input.GetKeyDown(KeyCode.D)) {
                Vector3 rotateVal = new Vector3(0, 90, 0);
                mainCamera.transform.Rotate(rotateVal);
            }
        }
    }

    // public void Update() {
    //     float xAxisValue = Input.GetAxis("Horizontal") * 0.05f;
    //     float zAxisValue = Input.GetAxis("Vertical") * 0.05f;
        
    //     if (Camera.current != null) {
    //         Camera.current.transform.Translate(new Vector3(0.0f, 0.0f, zAxisValue));
            
    //         Vector3 v3 = new Vector3(0, Input.GetAxis("Horizontal"), 0);
            
    //         transform.Rotate(v3 * 200f * Time.deltaTime);
    //     }
    // }
}
