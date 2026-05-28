import { useEffect, useState } from "react"
import { saveAs } from "file-saver"

function App() {

  const [prompt, setPrompt] = useState("")
  const [result, setResult] = useState(null)
  const [metrics, setMetrics] = useState(null)
  const [loading, setLoading] = useState(false)

  useEffect(() => {

    fetch("http://127.0.0.1:9001/evaluation-report")
      .then((res) => res.json())
      .then((data) => setMetrics(data))
      .catch((err) => console.error(err))

  }, [])

  const generateApp = async () => {

    setLoading(true)

    try {

      const response = await fetch(
        "http://127.0.0.1:9001/generate-app",
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json",
          },

          body: JSON.stringify({
            prompt: prompt,
          }),
        }
      )

      const data = await response.json()

      setResult(data)

    } catch (error) {

      console.error(error)

    }

    setLoading(false)
  }

  const downloadReport = () => {

    const blob = new Blob(

      [
        JSON.stringify(result, null, 2)
      ],

      {
        type: "application/json"
      }

    )

    saveAs(
      blob,
      "ai_app_report.json"
    )
  }

  return (

    <div className="min-h-screen bg-slate-950 text-white p-10">

      <div className="max-w-6xl mx-auto">

        <h1 className="text-5xl font-bold mb-3">
          AI App Compiler
        </h1>

        <p className="text-slate-400 mb-10">
          Generate full application architectures using AI pipelines.
        </p>

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-2xl">

          <textarea

            className="w-full h-40 bg-slate-950 border border-slate-700 rounded-xl p-4 text-white outline-none"

            placeholder="Describe your application idea..."

            value={prompt}

            onChange={(e) =>
              setPrompt(e.target.value)
            }

          />

          <button

            onClick={generateApp}

            className="mt-5 px-6 py-3 bg-blue-600 hover:bg-blue-700 rounded-xl font-semibold transition-all"
          >

            {
              loading
                ? "Generating..."
                : "Generate Application"
            }

          </button>

        </div>

        {
          metrics && (

            <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8 mt-10">

              <div className="bg-[#101935] p-5 rounded-2xl">
                <h3 className="text-gray-400 text-sm">
                  Total Tests
                </h3>

                <p className="text-3xl font-bold text-white mt-2">
                  {metrics?.total_tests}
                </p>
              </div>

              <div className="bg-[#101935] p-5 rounded-2xl">
                <h3 className="text-gray-400 text-sm">
                  Success Rate
                </h3>

                <p className="text-3xl font-bold text-green-400 mt-2">
                  {metrics?.success_rate}
                </p>
              </div>

              <div className="bg-[#101935] p-5 rounded-2xl">
                <h3 className="text-gray-400 text-sm">
                  Success Count
                </h3>

                <p className="text-3xl font-bold text-blue-400 mt-2">
                  {metrics?.success_count}
                </p>
              </div>

              <div className="bg-[#101935] p-5 rounded-2xl">
                <h3 className="text-gray-400 text-sm">
                  Failure Count
                </h3>

                <p className="text-3xl font-bold text-red-400 mt-2">
                  {metrics?.failure_count}
                </p>
              </div>

            </div>
          )
        }

        {
          result?.status === "clarification_required" && (

            <div className="mt-6 bg-yellow-500/10 border border-yellow-500 p-4 rounded-xl">

              <h2 className="text-yellow-400 text-xl font-bold mb-3">
                Clarification Needed
              </h2>

              <ul className="list-disc ml-6 text-gray-300">

                {
                  result.details.questions.map((q, index) => (

                    <li key={index}>
                      {q}
                    </li>

                  ))
                }

              </ul>

            </div>
          )
        }

        {
          result &&
          result.status !== "clarification_required" && (

            <button

              onClick={downloadReport}

              className="mt-8 px-6 py-3 bg-green-600 hover:bg-green-700 rounded-xl font-semibold transition-all"
            >

              Download Architecture Report

            </button>
          )
        }

        {
          result &&
          result.status !== "clarification_required" && (

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-10">

              <div className="bg-slate-900 p-6 rounded-2xl border border-slate-800">

                <h2 className="text-2xl font-bold mb-4">
                  Intent
                </h2>

                <pre className="text-sm text-slate-300 overflow-auto">
                  {JSON.stringify(result.intent, null, 2)}
                </pre>

              </div>

              <div className="bg-slate-900 p-6 rounded-2xl border border-slate-800">

                <h2 className="text-2xl font-bold mb-4">
                  Architecture
                </h2>

                <pre className="text-sm text-slate-300 overflow-auto">
                  {JSON.stringify(result.architecture, null, 2)}
                </pre>

              </div>

              <div className="bg-slate-900 p-6 rounded-2xl border border-slate-800">

                <h2 className="text-2xl font-bold mb-4">
                  Schema
                </h2>

                <pre className="text-sm text-slate-300 overflow-auto">
                  {JSON.stringify(result.schema, null, 2)}
                </pre>

              </div>

              <div className="bg-slate-900 p-6 rounded-2xl border border-slate-800">

                <h2 className="text-2xl font-bold mb-4">
                  Runtime Logs
                </h2>

                <pre className="text-sm text-slate-300 overflow-auto">
                  {JSON.stringify(result.runtime, null, 2)}
                </pre>

              </div>

            </div>
          )
        }

      </div>

    </div>
  )
}

export default App

