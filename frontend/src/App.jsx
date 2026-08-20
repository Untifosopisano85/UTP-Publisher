import { useState } from "react"
import "./App.css"


function App() {


  const [video, setVideo] = useState("")

  const [title, setTitle] = useState("")

  const [description, setDescription] = useState("")

  const [facebook, setFacebook] = useState("")

  const [instagram, setInstagram] = useState("")

  const [password, setPassword] = useState("")

  const [platforms, setPlatforms] = useState([
    "youtube",
    "facebook",
    "instagram"
  ])


  const [result, setResult] = useState({})

  const [status, setStatus] = useState("")

  const [uploading, setUploading] = useState(false)



  function togglePlatform(platform) {

    setPlatforms(prev =>

      prev.includes(platform)

        ? prev.filter(p => p !== platform)

        : [...prev, platform]

    )

  }



  async function uploadVideo(file) {


    const formData = new FormData()

    formData.append(
      "file",
      file
    )


    setUploading(true)


    const response = await fetch(
      "https://utp-publisher-production.up.railway.app/upload",
      {
        method: "POST",
        body: formData
      }
    )


    const data = await response.json()


    setVideo(data.path)

    setUploading(false)

  }



  async function publish() {


    setStatus(
      "Pubblicazione in corso..."
    )


    setResult({})



    const response = await fetch(

      "https://utp-publisher-production.up.railway.app/publish",

      {

        method: "POST",

        headers: {

          "Content-Type": "application/json"

        },


        body: JSON.stringify({

          video_path: video,

          platforms: platforms,

          password: password,

          youtube_title: title,

          youtube_description: description,

          facebook_message: facebook,

          instagram_caption: instagram


        })

      }

    )



    const data = await response.json()



    setResult(data)

    setStatus("")

  }




  return (

    <div className="container">


      <h1>
        UTP Publisher
      </h1>



      <div className="section">


        <h3>
          Video
        </h3>


        <input

          type="file"

          accept="video/*"

          onChange={
            e => uploadVideo(e.target.files[0])
          }

        />


        <p>

          {
            uploading
              ? "Caricamento video..."
              : video
                ? "Video pronto ✅"
                : ""
          }

        </p>


      </div>





      <div className="section">


        <h3>
          Testi
        </h3>



        <input

          placeholder="Titolo YouTube"

          value={title}

          maxLength={100}

          onChange={
            e => setTitle(e.target.value)
          }

        />


        <p>
          {title.length}/100
        </p>




        <textarea

          placeholder="Descrizione YouTube"

          value={description}

          onChange={
            e => setDescription(e.target.value)
          }

        />



        <textarea

          placeholder="Messaggio Facebook"

          value={facebook}

          onChange={
            e => setFacebook(e.target.value)
          }

        />



        <textarea

          placeholder="Caption Instagram"

          value={instagram}

          onChange={
            e => setInstagram(e.target.value)
          }

        />


      </div>





      <div className="section">


        <h3>
          Piattaforme
        </h3>



        <label>

          <input

            type="checkbox"

            checked={platforms.includes("youtube")}

            onChange={
              () => togglePlatform("youtube")
            }

          />

          YouTube

        </label>




        <label>

          <input

            type="checkbox"

            checked={platforms.includes("facebook")}

            onChange={
              () => togglePlatform("facebook")
            }

          />

          Facebook

        </label>





        <label>

          <input

            type="checkbox"

            checked={platforms.includes("instagram")}

            onChange={
              () => togglePlatform("instagram")
            }

          />

          Instagram

        </label>


      </div>



      <input

        type="password"

        placeholder="Password pubblicazione"

        value={password}

        onChange={
          (e) => setPassword(e.target.value)
        }

      />

      <button

        onClick={publish}

      >

        PUBBLICA

      </button>




      <p>

        {status}

      </p>




      <div className="result">


        <h3>
          Risultato
        </h3>



        {

          Object.entries(result).map(

            ([platform, data]) => (

              <p key={platform}>

                {
                  data.status === "success"
                    ? "🟢"
                    : "🔴"
                }

                {" "}

                {
                  platform.charAt(0).toUpperCase()
                  +
                  platform.slice(1)
                }

              </p>

            )

          )

        }


      </div>



    </div>

  )

}


export default App
