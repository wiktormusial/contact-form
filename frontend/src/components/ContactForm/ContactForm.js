import React, { useState } from 'react'
import { Formik, Form, Field } from 'formik';
import ClipLoader from "react-spinners/ClipLoader";
import { contactSend } from '../../api/contactSend'
import { ContactFormValidationSchema } from './ContactFormValidationSchema'
import { ContactFormSuccess } from './ContactFormSuccess'

export default function ContactForm() {
  const [status, setStatus] = useState("idle")

  function formSubmit(values) {
    setStatus("loading")
    contactSend(values)
      .then(() => setStatus("succeeded"))
  }

  if (status === "idle") {
    return (
      <div>
        <Formik
          initialValues={{
            author: '',
            title: '',
            body: '',
            category: 1,
          }}
          validationSchema={ContactFormValidationSchema}
          onSubmit={(values) => formSubmit(values)}
        >
        {({ errors, touched }) => (
          <Form>
            <div className="form-element">
              <label htmlFor="author">Email</label>
              <Field className="form-control" type="email" name="author"/>
              {errors.author && touched.author && <div className="form-text">{errors.author}</div>}
            </div>
            <div className="form-element">
              <label htmlFor="title">Title</label>
              <Field className="form-control" type="text" name="title"/>
              {errors.title && touched.title && <div className="form-text">{errors.title}</div>}
            </div>
            <div className="form-element">
              <label htmlFor="body">Content</label>
              <Field className="form-control" name="body" as="textarea"/>
              {errors.body && touched.body && <div className="form-text">{errors.body}</div>}
            </div>
            <div className="form-element">
              <label htmlFor="category">Category</label>
              <Field className="form-select" name="category" as="select">
                <option value="1">Cooperation Proposal</option>
              </Field>
            </div>
            <div className="form-element">
              <button type="submit" className="btn btn-primary">
                Submit
              </button>
            </div>
          </Form>
        )}
        </Formik>
      </div>
    )
  } else if (status === "loading") {
    return(
      <div className="spinner">
        <ClipLoader size={100} color={"#EE7788"} speedMultiplier={"0.7"}/>
      </div>
    )
  } else if (status === "succeeded") {
    return (
      <ContactFormSuccess />
    )
  }
}
