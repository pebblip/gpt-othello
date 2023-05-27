/**
 * This file was auto-generated by openapi-typescript.
 * Do not make direct changes to the file.
 */


export interface paths {
  "/start": {
    /**
     * ゲームの開始 
     * @description このエンドポイントはオセロゲームを開始します。ゲーム状態が初期化され、初期盤面がレスポンスとして返されます。
     */
    get: operations["start_start_get"];
  };
  "/user/place": {
    /**
     * ユーザの石の配置 
     * @description ユーザーが石を置く位置を指定してこのエンドポイントにリクエストを送信します。その位置に石を置いた後のゲーム盤面をレスポンスとして返します。
     */
    post: operations["user_place_user_place_post"];
  };
  "/user/pass": {
    /**
     * ユーザのパス 
     * @description ユーザーがパスを宣言してこのエンドポイントにリクエストを送信します。その後、AIが石を置く位置を計算し、その位置に石を置いた後のゲーム盤面をレスポンスとして返します。
     */
    post: operations["user_pass_user_pass_post"];
  };
  "/ai/place": {
    /**
     * AIの石の配置 
     * @description このエンドポイントを呼び出すと、AIが次に石を置く位置を計算し、その位置に石を置いた後のゲーム盤面がレスポンスとして返されます。
     */
    post: operations["ai_place_ai_place_post"];
  };
  "/gpt/ask": {
    /**
     * ChatGPTに次の手を尋ねる 
     * @description ChatGPTに次の手を尋ね、最善手を返します。
     */
    post: operations["start_gpt_ask_post"];
  };
}

export type webhooks = Record<string, never>;

export interface components {
  schemas: {
    /** Board */
    Board: {
      /**
       * 盤面サイズ 
       * @description 盤面のサイズ 
       * @example 8
       */
      size: number;
      /**
       * 盤面 
       * @description 2次元配列で表現したオセロ盤面。1:黒,-1:白 
       * @example [[0, 0],[0, 1], [-1, 0], [0, 0]]
       */
      rows: ((number)[])[];
      /**
       * 次に置き石可能な位置のリスト 
       * @description 左上を(0,0)都する座標のリスト 
       * @example [(0, 0), (0, 1), (0, 2)]
       */
      valids: ([number,number])[];
      /**
       * 盤面状態 
       * @description 0:続行中, 1:黒の勝ち,2:白の勝ち,3:引き分け 
       * @example 0
       */
      status: components["schemas"]["GameStatus"];
      /**
       * スコア 
       * @description 黒と白の石の数 
       * @example [2, 2]
       */
      score: (number)[];
    };
    /**
     * GameStatus 
     * @description An enumeration. 
     * @enum {integer}
     */
    GameStatus: 0 | 1 | 2 | 3;
    /** GptAnswer */
    GptAnswer: {
      /**
       * 最善手 
       * @description 次の指し手を表す座標位置 
       * @example (0, 0)
       */
      position: [number,number];
      /**
       * 最善手の説明 
       * @description 次の指し手の説明 
       * @example 左上に置く
       */
      answer: string;
    };
    /** HTTPValidationError */
    HTTPValidationError: {
      /** Detail */
      detail?: (components["schemas"]["ValidationError"])[];
    };
    /** ValidationError */
    ValidationError: {
      /** Location */
      loc: (string | number)[];
      /** Message */
      msg: string;
      /** Error Type */
      type: string;
    };
  };
  responses: never;
  parameters: never;
  requestBodies: never;
  headers: never;
  pathItems: never;
}

export type external = Record<string, never>;

export interface operations {

  /**
   * ゲームの開始 
   * @description このエンドポイントはオセロゲームを開始します。ゲーム状態が初期化され、初期盤面がレスポンスとして返されます。
   */
  start_start_get: {
    responses: {
      /** @description Successful Response */
      200: {
        content: {
          "application/json": components["schemas"]["Board"];
        };
      };
    };
  };
  /**
   * ユーザの石の配置 
   * @description ユーザーが石を置く位置を指定してこのエンドポイントにリクエストを送信します。その位置に石を置いた後のゲーム盤面をレスポンスとして返します。
   */
  user_place_user_place_post: {
    parameters: {
      query: {
        /** @description 石を置くX座標 */
        x: number;
        /** @description 石を置くY座標 */
        y: number;
      };
    };
    requestBody: {
      content: {
        /** @example [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,-1,1,0,0,0],[0,0,0,1,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]] */
        "application/json": ((number)[])[];
      };
    };
    responses: {
      /** @description Successful Response */
      200: {
        content: {
          "application/json": components["schemas"]["Board"];
        };
      };
      /** @description Validation Error */
      422: {
        content: {
          "application/json": components["schemas"]["HTTPValidationError"];
        };
      };
    };
  };
  /**
   * ユーザのパス 
   * @description ユーザーがパスを宣言してこのエンドポイントにリクエストを送信します。その後、AIが石を置く位置を計算し、その位置に石を置いた後のゲーム盤面をレスポンスとして返します。
   */
  user_pass_user_pass_post: {
    requestBody: {
      content: {
        /** @example [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,-1,1,0,0,0],[0,0,0,1,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]] */
        "application/json": ((number)[])[];
      };
    };
    responses: {
      /** @description Successful Response */
      200: {
        content: {
          "application/json": components["schemas"]["Board"];
        };
      };
      /** @description Validation Error */
      422: {
        content: {
          "application/json": components["schemas"]["HTTPValidationError"];
        };
      };
    };
  };
  /**
   * AIの石の配置 
   * @description このエンドポイントを呼び出すと、AIが次に石を置く位置を計算し、その位置に石を置いた後のゲーム盤面がレスポンスとして返されます。
   */
  ai_place_ai_place_post: {
    requestBody: {
      content: {
        /** @example [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,-1,1,0,0,0],[0,0,0,1,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]] */
        "application/json": ((number)[])[];
      };
    };
    responses: {
      /** @description Successful Response */
      200: {
        content: {
          "application/json": components["schemas"]["Board"];
        };
      };
      /** @description Validation Error */
      422: {
        content: {
          "application/json": components["schemas"]["HTTPValidationError"];
        };
      };
    };
  };
  /**
   * ChatGPTに次の手を尋ねる 
   * @description ChatGPTに次の手を尋ね、最善手を返します。
   */
  start_gpt_ask_post: {
    requestBody: {
      content: {
        /** @example [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,-1,1,0,0,0],[0,0,0,1,-1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]] */
        "application/json": ((number)[])[];
      };
    };
    responses: {
      /** @description Successful Response */
      200: {
        content: {
          "application/json": components["schemas"]["GptAnswer"];
        };
      };
      /** @description Validation Error */
      422: {
        content: {
          "application/json": components["schemas"]["HTTPValidationError"];
        };
      };
    };
  };
}
