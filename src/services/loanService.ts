import { ENDPOINTS } from "@/config/api";

export interface PredictionResult {
  prediction_text: string;
  confidence: number;
  risk_level: string;
  explanation_text: string;
  chart_labels: string[];
  chart_values: number[];
}



export async function predictLoan(formData: Record<string, string>): Promise<PredictionResult> {
  const body = new URLSearchParams(formData);

  const response = await fetch(ENDPOINTS.predict, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: body.toString(),
  });

  if (!response.ok) {
    throw new Error("Prediction request failed");
  }

  return response.json();
}

export async function chatWithAI(message: string): Promise<string> {
  try {
    const response = await fetch(ENDPOINTS.chat, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });

    const data = await response.json();

    // Accept either reply or message
    return data.reply || data.message || "No response from AI.";
  } catch (error) {
    console.error("Chat error:", error);
    throw new Error("Chat request failed");
  }
}
